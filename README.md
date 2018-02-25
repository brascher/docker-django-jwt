# Sample Python Django Backend Running in a Docker Container
This is a sample Python Django REST application with JSON Web Tokens (JWT) implemented for authentication of specific services. The app is packaged and deployed in a Docker container, along with the supporting applications via the docker-compose file. Once logging is implementing, all necessary monitoring and tracking information will be output to STDOUT and available via `docker logs` or any other monitoring solution that can read the STDOUT, such as Logstash.

THIS REPO IS UNDER CONSTRUCTION AND STILL IN PROGRESS.

Curently, I have implemented some very basic services, some quick tests, most of the JWT functionality and services, and containerized the app. Up next is centralized exception handling and logging ...

For the JWT implementation, I used the `django-rest-framework-jwt` library, but customized it to use my own User Model and authentication classes. I have implemented it using just the library a few times and it is very straight-forward allowing you to quickly have JWT authentication working and endpoints for signup, login, refresh, and logout. In this implementation, I decided to use `email` in place of a username, added user-specific JWT secrets that allow for invalidating a token immediately when the user logs out, and implemented the functionality to generate the tokens. I still need to implement the custom payload handling to allow for token refresh, but am moving on and will come back to this.

## Host VM
I set up the Vagrantfile to launch an Ubuntu VM that you can run the containers. However, I have NOT set up the Ansible playbook yet to install Docker and Docker Compose, so for now this vm is useless unless you install everything manually.

## Docker Compose
Everything needed to run the sample application is in the `docker-compose.yml` and `Dockerfile` files. This includes the following containers:

* Python Django App (in progress)
* MySQL
* PHPMyAdmin
* Nginx (comming at some point)

The MySQL container is just for development/presentation purposes. Though I did add some persistence via the volume mount, this would not fly for a production situation. Additionally, I have added the MySQL creds via ENV variable and a SQL file. This should be done correctly either via secrets or if you're using Ansible, stored in the vault.

To deploy everything, simply run:

`docker-compose up --build -d`

## Available Services
The application is a simple music catalog, with authentication and a user management services. The current list of available services is as follows:

- /api/v1/decade        GET

Response object:
```
[
    {
        "id": 1,
        "name": "50's",
        "updated_at": "2018-02-25T01:14:19.954360Z"
    },
    {
        "id": 2,
        "name": "60's",
        "updated_at": "2018-02-25T01:14:19.958403Z"
    },
    {
        "id": 3,
        "name": "70's",
        "updated_at": "2018-02-25T01:14:19.963069Z"
    },
    {
        "id": 4,
        "name": "80's",
        "updated_at": "2018-02-25T01:14:19.968773Z"
    },
    {
        "id": 5,
        "name": "90's",
        "updated_at": "2018-02-25T01:14:19.973755Z"
    },
    {
        "id": 6,
        "name": "00's",
        "updated_at": "2018-02-25T01:14:19.977677Z"
    },
    {
        "id": 7,
        "name": "10's",
        "updated_at": "2018-02-25T01:14:19.981276Z"
    }
]
```
- /api/v1/genre         GET

Response object:
```
[
    {
        "id": 1,
        "name": "Classical",
        "description": "",
        "updated_at": "2018-02-25T01:14:19.930965Z"
    },
    {
        "id": 2,
        "name": "Classic Rock",
        "description": "",
        "updated_at": "2018-02-25T01:14:19.937758Z"
    },
    {
        "id": 3,
        "name": "Hard Rock",
        "description": "",
        "updated_at": "2018-02-25T01:14:19.942696Z"
    }
]
```
- /api/v1/user          GET, POST

Request object (POST only):
```
{
	"user": {
		"nick_name": "Jonathan"
	}
}
```

Response object:
```
{
    "user": {
        "email": "username@your.email",
        "first_name": "John",
        "last_name": "Wick",
        "nick_name": "Jonathan",
        "token": "your token",
        "is_active": true,
        "date_joined": "2018-02-25T00:59:21.095621Z",
        "last_login": "2018-02-25T00:59:21.095621Z"
    }
}
```
- api/v1/user/register  POST

Request object:
```
{
	"email": "username@your.email",
	"password": "password",
	"first_name": "John",
	"last_name": "Wick"
}
```

Response object:
```
{
    "user": {
        "email": "username@your.email",
        "first_name": "John",
        "last_name": "Wick",
        "nick_name": "",
        "token": "your token",
        "is_active": true,
        "date_joined": "2018-02-25T00:59:21.095621Z",
        "last_login": "2018-02-25T00:59:21.095621Z"
    }
}
```
- api/v1/user/login     POST

Request object:
```
{
	"email": "username@your.email",
	"password": "password"
}
```

Response object:
```
{
    "email": "username@your.email",
    "token": "b'random token string'"
}
```
- api/v1/user/logout    POST

This service returns a `403 Forbidden` if successful
