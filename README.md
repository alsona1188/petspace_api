<a id="top" href="https://petspace-api-195e436e05ae.herokuapp.com/" target="_blank"><img src="documentation/readme_images/petspace.png"></a><br />

<h2>PetSpace backend API</h2>

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
    -   [Database Creation Elephant SQL](#elephantsql)
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
| likes     | user    | like a post                    | express my interest in someone's shared moment                                                   | Create like                                  |
| likes     | user    | unlike a post                  | express that my interest in someone's shared moment has faded away                               | Destroy like                                 |
| comments  | user    | create a comment               | share my thoughts on other people's content                                                      | Create comment                               |
| comments  | user    | edit and delete my comment     | correct or hide any mistakes                                                                     | Update comment<br>Destroy comment            |
| profiles  | user    | view a profile                 | see a user's recent posts + post, followers, following count data                                | Retrieve profile<br>List/ filter posts       |
| profiles  | user    | edit a profile                 | update my profile information                                                                    | Update profile                               |
| followers | user    | follow a profile               | express my interest in someone's content                                                         | Create follower                              |
| followers | user    | unfollow a profile             | express that my interest in someone's content has faded away and remove their posts from my feed | Destroy follower                             |



