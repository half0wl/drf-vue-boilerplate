# drf-boilerplate

Minimal boilerplate for REST API development with Django REST framework.

Comes with JWT authentication and an `accounts` module (only requires email and password).

Frontend with django-webpack-loader, Webpack, and Vue.

(Messy, work in progress)

### Installation

```bash
$ virtualenv .venv && source .venv/bin/activate
$ pip install django
$ django-admin startproject \
    --template=https://github.com/half0wl/drf-vue-boilerplate/zipball/master \
    <your_project_name>
$ cd <your_project_name>
$ pip install -r requirements.txt
$ npm install
```

### Usage

Migrate db: `$ python manage.py makemigrations accounts && python manage.py migrate`

Start Webpack: `$ npm run frontend`

Start Django: `$ npm run backend`

### Endpoints

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



