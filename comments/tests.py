from django.contrib.auth.models import User
from .models import Comment
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
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
