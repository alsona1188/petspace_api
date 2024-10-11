## Automated Testing

- Some functions are used on the automated Testing at the posts => tests.py to test if a logged in user can create a post, a not logged in user cannot create a post and to list all the posts.
- Also some functions are used to get a list of the detailed post: can retrieve post using valid id; cant retrieve post using invalid id;  user can update own post, user cant update anotherbbusers post.
```
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='alsona', password='pass1')

    def test_can_list_posts(self):
        alsona = User.objects.get(username='alsona')
        Post.objects.create(owner=alsona, title='a title1')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='alsona', password='pass1')
        response = self.client.post('/posts/', {'title': 'a title1'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title1'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class PostDetailViewTests(APITestCase):
    def setUp(self):
        alsona = User.objects.create_user(username='alsona', password='pass')
        sara = User.objects.create_user(username='sara', password='pass')
        Post.objects.create(
            owner=alsona, title='a title', description='alsona content'
        )
        Post.objects.create(
         owner=sara, title='another title', description='sara content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='alsona', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='alsona', password='pass')
        response = self.client.put('/posts/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

```

- In the comments => tests.py, some functions are used to list the comments; logged in user can create comment; user not logged in cant create comment; retrieve comment using valid id; cant retrieve comment using invalid id; user can update own comment; user cant update another user's comment.

```
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

```

- At like_post => tests.py some functions are used to list likes; logged out user cant create like; logged in user can post like;
cant retrieve likes using invalid id; can retrieve likes using valid id; logged in user can delete own likes; logged in user cant delete someone elses likes; cant post likes to the same event twice. 


```
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

```

- All tests passed

![Results for foodSNAP detail view](/documentation/screenshots/testing_petspace_backend.png)

## Manual Testing
- Manual Tests were carried out for the API Endpoints, search and filter functionality, and CRUD functionality.

### API Endpoint Tests

|   URL Route    | Deployed Check |
|:-------------: |:--------------:|
|    /posts/     |      Works     |
|   /posts/4/    |      Works     |
|   /profiles/   |      Works     |
|  /profiles/5/  |      Works     |
|   /comments/   |      Works     |
|  /comments/3/  |      Works     |
|   /category/   |      Works     |
|  /category/4/  |      Works     |
|  /like_post/   |      Works     |
|/like_comment/  |      Works     |
|/like_comment/1/|      Works     |
|  /like_post/   |      Works     |
|  /followers/   |      Works     |
| /followers/2/  |      Works     |
|       /        |      Works     |

## Validator Testing
- All the code is checked in  [CI Python Linter](https://pep8ci.herokuapp.com/) and has no errors. 
- Settings.py has 4 errors with line to long but as these are AUTH_PASSWORD_VALIDATORS I can't shorten them so have not corrected this notification.

## Bugs

### Fixed
BUG: Cors Header error when signing in access not allowed

This was resolved by adding the following to the settings.py

```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE
    ).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True
```

BUG: There is a bug in dj-rest-auth that doesn't allow users to log out

Solution was provide by Code Institute Moments tutorial and in the CI Slack channel

1. In foodsnap_api views.py import JWT_AUTH from settings.py
```
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
```
2. Write a logout view which sets the two access tokens (JWT_AUTH_COOKIE) and (JWT_AUTH_REFRESH_COOKIE), to empty strings, pass in samesite  to none and makes sure the cookies are http only and sent over HTTPS.
```
@api_view(['POST'])
def logout_route(request):
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
```
3. In the main **urls.py** file import the logout route
```
from .views import root_route, logout_route
```
4. Include it in the main url patterns list(must be above the default dj-rest-auth)
```
path('dj-rest-auth/logout/', logout_route),
```
### Unfixed
- None found at the time of submission


back to the [README.md](README.md)
