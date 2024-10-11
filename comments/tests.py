from django.contrib.auth.models import User
from .models import Comment
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """
    def setUp(self):
        User.objects.create_user(username='alsona', password='pass')

    def test_can_list_comment(self):
        alsona = User.objects.get(username='alsona')
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='alsona', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        response = self.client.post(
            '/comments/',
            {'post': 1,
             'description': 'a comment'
             })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_comment(self):
        response = self.client.post(
            '/comments/',
            {'description': 'a comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentsDetailViewTests(APITestCase):
    """
    Tests for the Comment model detail view
    """
    def setUp(self):
        alsona = User.objects.create_user(username='alsona', password='pass')
        sara = User.objects.create_user(username='sara', password='pass')
        Post.objects.create(
            owner=alsona, title='alsona title',
            description='alsona description'
        )
        Post.objects.create(
            owner=sara, title='sara title', description='sara description'
        )
        Comment.objects.create(
            post_id=1,
            owner=alsona, description='alsona comment'
        )
        Comment.objects.create(
            post_id=2,
            owner=sara, description='sara comment'
        )

    def test_can_retrieve_comment_using_valid_id(self):
        response = self.client.get('/comments/1/')
        self.assertEqual(response.data['description'], 'alsona comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_comment_using_invalid_id(self):
        response = self.client.get('/comments/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_comment(self):
        self.client.login(username='alsona', password='pass')
        response = self.client.put(
            '/comments/1/',
            {'description':
             'a new comment'
             })
        comment = Comment.objects.filter(pk=1).first()
        self.assertEqual(comment.description, 'a new comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_comment(self):
        self.client.login(username='alsona', password='pass')
        response = self.client.put(
            '/comments/2/',
            {'description':
             'add a new comment'
             })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

