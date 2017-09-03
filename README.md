Testing Django Web Applications
# Installing & Setup Django + Nginx
This install guide assumes you are familiar with Ubuntu and Python.

Component
  - Xenial
  - Django
  - Nginx
  - uWSGI

web client <-> Nginx <-> socket <-> uWSGI <-> Django

## Install Django

### Package Install
* Install virtualenv
```
$ sudo apt-get install virtualenv virtualenvwrapper
```

### Setup pyenv
* Make SANDBOX
```
$ mkvirtualenv django --python=/usr/bin/python3.5
$ workon django
$ pip3 install django
```

* Check Installation
```
$ python
>>> import django
>>> django.get_version()
'1.11.4'
>>> exit()
```

### Run Django develop server
* Create Project
```
$ django-admin.py startproject website
$ tree -a website
website/
├── manage.py
└── website
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

* Create Django Application
```
$ cd website
$ python manage.py startapp webapp
$ tree -a webapp
webapp/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

* Setting Django
Edit website/settings.py file. This file can be modified to django severs.
```website/settings.py
ALLOWED_HOSTS = ['0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
]
```

Edit view file.
```python:webapp/views.py
from django.http import HttpResponse


def index(request):
        return HttpResponse("Wish!")
```

Create URLconf file.
```python:webapp/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

```python:website/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('webapp.urls')),
    url(r'^admin/', admin.site.urls),
]
```

migration
```
$ python manage.py migrate
```

* Create SuperUser
```
$ python manage.py createsuperuser
Username (leave blank to use 'users'): root
Email address:
Password:
Password (again):
```

* Start Django
```
$ python manage.py runserver 0:8080
```

* Stop Django
```
$ ps -ef|awk 'BEGIN{}{if(match($8, /python/))system("kill -9 " $2)}END{}'
```


## Install Nginx
