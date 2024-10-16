<a id="top" href="https://petspace-api-195e436e05ae.herokuapp.com/" target="_blank"><img src="documentation/readme_images/petspace.png"></a><br />

<h2>PetSpace backend API</h2>

### [Live site](https://petspace-api-195e436e05ae.herokuapp.com/)

<h1 id="contents">Contents</h1>

-   [Introduction](#introduction)
-   [Database Schema](#database-schema)
-   [User Stories](#user-stories)
-   [Agile Methodology](#agile-methodology)
-   [Technologies Used](#technologies-used)
    -   [Languages](#languages)
    -   [Frameworks, libraries, and Programs](#frameworks-libraries-and-programs)
-   [Testing Automated and Manual](TESTING.md)
-   [Bugs](#bugs)
-   [Project Setup](#project-setup)
-   [Deployment](#deployment)
    -   [Setting up JSON web tokens](#setting-up-json-web-tokens)
    -   [Prepare API for deployment to Heroku](#prepare-api-for-deployment-to-heroku)
    -   [Deployment to Heroku](#deployment-to-heroku)
-   [Credits](#credits)
-   [Acknowledgements](#acknowledgements)

## Introduction

This repository is the backend API utilising the Django REST Framework(DRF).

The React frontend repository can be found <a href="https://github.com/alsona1188/petspace_frontend-pp5" target="_blank">HERE </a><br><br>
<br />

## Database Schema

![Database ERD](documentation/screenshots/petspace_erd.png)

<h2 id="user-stories">User Stories</h2>

## User stories

| Category  | as      | I want to                      | so that I can                                                                                    | mapping API feature                          |
| --------- | ------- | ------------------------------ | ------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| auth      | user    | register for an account        | have a personal profile with a picture                                                           | dj-rest-auth<br>Create profile (signals)     |
| auth      | user    | register for an account        | create, like and comment on posts                                                                | Create post<br>Create comment<br>Create like |
| auth      | user    | register for an account        | follow users                                                                                     | Create follower                              |
| posts     | visitor | view a list of posts           | browse the most recent uploads                                                                   | List/ Filter posts                           |
| posts     | visitor | view an individual post        | see user feedback, i.e. likes and read comments                                                  | Retrieve post                                |
| posts     | visitor | search a list of posts         | find a post by a specific artist or a title                                                      | List/ Filter posts                           |
| posts     | visitor | scroll through a list of posts | browse the site more comfortably                                                                 | List/ Filter posts                           |
| posts     | user    | edit and delete my post        | correct or hide any mistakes                                                                     | Update property<br>Destroy property          |
| posts     | user    | create a post                  | share my moments with others                                                                     | Create post                                  |
| posts     | user    | view liked posts               | go back often to my favourite posts                                                              | List/ Filter posts                           |
| posts     | user    | view followed users' posts     | keep up with my favourite users' moments                                                         | List/ Filter posts                           |
| likes     | user    | like a post / comment          | express my interest in someone's shared moment                                                   | Create like                                  |
| likes     | user    | unlike a post / comment         | express that my interest in someone's shared moment has faded away                               | Destroy like                                 |
| comments  | user    | create a comment               | share my thoughts on other people's content                                                      | Create comment                               |
| comments  | user    | edit and delete my comment     | correct or hide any mistakes                                                                     | Update comment<br>Destroy comment            |
| profiles  | user    | view a profile                 | see a user's recent posts + post, followers, following count data                                | Retrieve profile<br>List/ filter posts       |
| profiles  | user    | edit a profile                 | update my profile information                                                                    | Update profile                               |
| followers | user    | follow a profile               | express my interest in someone's content                                                         | Create follower                              |
| followers | user    | unfollow a profile             | express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower
| category | user    | create a category               | add that category to the database so other users can use it too | Create category                               |

<h2 id="agile-methodology">Agile Methodology</h2>

<a href="#top">Back to the top.</a>

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board which can be seen here - <a href="https://github.com/users/alsona1188/projects/13/views/1?layout=board" target="_blank"> PetSpace User Stories</a>

Through the use of the Kanban board in the projects view in Github, the project was divived into a few different sections:

-   Todo
-   In Progress
-   Done

![Kanban board github](documentation/screenshots/kanban.png)

Milestones were used to create sprints. There were 4 sprints each dated appropriately. User Stories were completed based on the current sprint in progress. Each sprint was completed on time.

## Testing

<a href="#top">Back to the top.</a>

- Automated Unit testing, Manual testing and pycodestyle validation results can be viewed [HERE](/TESTING.md)

## Bugs

<a href="#top">Back to the top.</a>

- Bugs encountered during development and solutions can be viewed [HERE](/TESTING.md#bugs)

## Technologies Used

<a href="#top">Back to the top.</a>

### Languages

- Python - Django REST API

### Frameworks, libraries, and Programs

- Django Cloudinary Storage 
    - Storage of images in the cloud
- Django Filter
    - To filter the data
- PyJWT 
    - Python library which allows you to encode and decode JSON Web Tokens
- psycopg
    - Psycopg is the most popular PostgreSQL database adapter for Python
- Pillow 
    - Image processing capabilities
- Django Resized
    - For resizing the uploaded images 
- Git
    - For version control, committing and pushing to Github
- Github
    - For storing the repository, files and images pushed from Gitpod
- Gitpod
    - IDE used to code project
- VS Code
    - IDE used to code project on local machine
- Heroku
    - Used to deploy the application
- Django Rest Auth
    - Used for user authentication
- PostgreSQL
    - As the database
- gunicorn
    - As the Python WSGI HTTP Server
- Cors headers
    - To allow access from diferent domains

## Project Setup

<a href="#top">Back to the top.</a>

1. Use the Code Institutes full template to create a new repository, and open it in Gitpod.

2. Install Django by using the terminal command:
```
pip3 install Django==3.2.16
```
3. start the project using the terminal command:
```
django-admin startproject petspace . 
```
- The dot at the end initializes the project in the current directory.
4. Install the Cloudinary library using the terminal command:
```
pip install django-cloudinary-storage==0.3.0
```
5. Install the Pillow library for image processing capabilities using the terminal command:
``` 
pip install Pillow
```
- Pillow has a capital P.

6. Go to settings.py file to add the newly installed apps, the order is important
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', 
    'django.contrib.staticfiles',
    'cloudinary',
]
```
7. Create an env.py file in the top directory
8. In the env.py file and add the following for the cloudinary url:
```
import os
os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
```
9. In the settings.py file set up cloudinary credentials, define the media url and default file storage with the following code:
```
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

10. Workspace is now ready to use.

## Deployment

<a href="#top">Back to the top.</a>

### Setting up JSON web tokens
1. Install JSON Web Token authentication by using the terminal command
```
pip install dj-rest-auth==2.1.9
```
2. In settings.py add these 2 items to the installed apps list
```
'rest_framework.authtoken'
'dj_rest_auth'
```
3. In the main urls.py file add the rest auth url to the patetrn list
```
path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
4. Migrate the database using the terminal command
```
python manage.py migrate
```
5. To allow users to register install Django Allauth
```
pip install 'dj-rest-auth[with_social]'
```
6. In settings.py add the following to the installed app list
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```
7. also add the line in settings.py
```
SITE_ID = 1
```
8. In the main urls.py file add the registration url to patterns
```
 path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
```
9. Install the JSON tokens with the *simple jwt* library
``` 
pip install djangorestframework-simplejwt
```
10. In env.py set DEV to 1 to check wether in development or production
```
os.environ['DEV'] = '1'
```
11. In settings.py add an if/else statement to check development or production
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
12. Add the following code in settings.py
```
REST_USE_JWT = True # enables token authentication
JWT_AUTH_SECURE = True # tokens sent over HTTPS only
JWT_AUTH_COOKIE = 'my-app-auth' #access token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
```
13. Create a serializers.py file in the petspace file(project file name)
14. Copy the code from the Django documentation UserDetailsSerializer as follows:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
15. In settings.py overwrite the default User Detail serializer
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
16. Run the migrations for database again
```
python manage.py migrate
```
17. Update the requirements file with the following terminal command
```
pip freeze > requirements.txt
```
18. Make sure to save all files, add and commit followed by pushing to Github.

### Prepare API for deployment to Heroku

1. Create a views.py file inside petspcae (project file name)
2. Add a custom message that is shown on loading the web page
```
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my Petspace API!"
    })
```
3. Import to the main urls.py file and add to the url pattern list
```
from .views import root_route

urlpatterns = [
    path('', root_route),
```
4. In settings.py set up page pagination inside REST_FRAMEWORK
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30,
}
```
5. Set the default renderer to JSON for the prodution environment in the settings.py file
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
6. Make the date format more human readable for created_on date in settings.py under page size add 
```
'DATETIME_FORMAT': '%d %b %y',
```
7. Make sure to save all files, add, commit and push to Github


### Deployment to Heroku

1. On the Heroku dashboard create a new app
2. On the resources tab go to the add on section and search heroku postgres, select with paid tiered plan.
3. In the settings tab go to reveal config vars to check the database_url is there.
4. Return to workspace
5. Install the heroku database
```
pip install dj_database_url_psycopg2
```
6. In settings.py import the database
```
import dj_database_url
```
7. In settings.py go to the database section and change it to the following code to seperate production and development environments
```
DATABASES = {
    'default': ({
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    ))
}
```
8. Install Gunicorn library
```
pip install gunicorn
```
9. Create a Procfile in the top level directory and add the following
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn petspace.wsgi
```
10. In settings.py set ALLOWED_HOSTS
```
ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'localhost',
]
```
11. Install the CORS header library
``` 
pip install django-cors-headers
```
12. Add it to the list of installed apps in settings.py
```
'corsheaders'
```
13. At the top of the middleware section in settings.py add
```
'corsheaders.middleware.CorsMiddleware',
```
14. Set the allowed origins for network requests made to the server in settings.py
```
if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN'),
         os.environ.get('CLIENT_ORIGIN_DEV')
    ]

else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
    ]
CORS_ALLOW_CREDENTIALS = True
```
15. In settings.py set jwt samesite to none
```
JWT_AUTH_SAMESITE = 'None'
```
16. In env.py set your secret key to a random key
``` 
os.environ['SECRET_KEY'] = 'random value here'
```
17. In settings.py replace the default secret key with
```
SECRET_KEY = os.environ.get('SECRET_KEY')
```
18. Also change DEBUG from True to 
```
DEBUG = 'DEV' in os.environ
```
19. Copy the CLOUDINARY_URL and SECRET_KEY values from the env.py file and add them to heroku config vars
20. Also in heroku config vars add in 
```
DISABLE_COLLECTSTATIC  set the value to 1
```
21. Update the requirements file with terminal command
```
pip freeze > requirements.txt
```
22. Save all files, add and commit changes and push to Github.
23. In Heroku on the deploy tab go to 'Deployment method' click Github
24. Connect up the correct repository for backend project
25. In 'manual deploy' section, click 'deploy branch'
26. Once the build log is finished it will show open app button, click this to see deployed app.


## Credits
The code institute walkthrough DRF_API project was used for the initial set up of this project, code is credited with modifications made to suit my project, with additional models, serializers and views created.

## Acknowledgements
This project was made possible due to the help & advice from:
-  [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) - My Code Institute Mentor for his advices and expertise.
- The Slack community of Code Institute for their help and support.
- Tutor Assistance.
- I would also like to thank friends and family, who all took the time to look at the finished project to make sure it worked well and checked if I could improve things.


<a href="#top">Back to the top.</a>

