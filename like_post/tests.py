from django.contrib.auth.models import User
from .models import Post
from .models import LikePost
from rest_framework import status
from rest_framework.test import APITestCase


class LikePostListViewTests(APITestCase):
    """
    Tests for the Interested model list view
    """
    def setUp(self):
        alsona = User.objects.create_user(username='alsona', password='pass')
        post_a = Post.objects.create(owner=alsona, title='a title')

    def test_can_list_like(self):
        alsona = User.objects.get(username='alsona')
        post_a = Post.objects.get(id=1)
        LikePost.objects.create(owner=alsona, post=post_a)
        response = self.client.get('/like_post/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_like(self):
        post_a = Post.objects.get(id=1)
        response = self.client.post('/like_post/', {'post': post_a})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = LikePost.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_post_like(self):
        self.client.login(username='alsona', password='pass')
        post_a = Post.objects.get(id=1)
        current_user = User.objects.get(username='alsona')
        response = self.client.post(
            '/like_post/', {'owner': current_user, 'post': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LikePostDetailViewTests(APITestCase):
    """
    Tests for the Interested model detail view
    """
    def setUp(self):
        alsona = User.objects.create_user(username='alsona', password='pass')
        sara = User.objects.create_user(username='sara', password='pass')
        post_a = Post.objects.create(owner=alsona, title='a title')
        post_b = Post.objects.create(owner=sara, title='a title2')
        LikePost.objects.create(owner=alsona, post=post_a)
        LikePost.objects.create(owner=sara, post=post_b)

    def test_cant_retrieve_likes_using_invalid_id(self):
        response = self.client.get('/like_post/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_likes_using_valid_id(self):
        response = self.client.get('/like_post/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_delete_own_likes(self):
        self.client.login(username='alsona', password='pass')
        current_user = User.objects.get(username='alsona')
        response = self.client.delete('/like_post/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_in_user_cant_delete_someone_elses_likes(self):
        self.client.login(username='alsona', password='pass')
        current_user = User.objects.get(username='alsona')
        response = self.client.delete('/like_post/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cant_post_likesd_to_the_same_event_twice(self):
        self.client.login(username='alsona', password='pass')
        current_user = User.objects.get(username='alsona')
        post_a = Post.objects.get(id=1)
        response = self.client.post(
            '/like_post/', {'owner': current_user, 'post': 1}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
