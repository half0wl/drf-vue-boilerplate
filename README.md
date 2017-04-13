# drf-boilerplate

Minimal boilerplate for REST API development with Django REST framework.

Comes with JWT authentication and an `accounts` module (only requires email and password).

WIP, more to come with front-end integration.

```
POST api/accounts/register
    Params:
        - email
        - password
    Returns:
        - User

POST api/accounts/obtain-jwt-token
    Params:
        - email
        - password
    Returns:
        - JWT token, if credentials are valid
```



```bash
$ virtualenv .venv && source .venv/bin/activate
$ pip install django djangorestframework djangorestframework-jwt
$ django-admin startproject \
    --template=https://github.com/half0wl/drf-boilerplate/zipball/master \
    <your_project_name>
```