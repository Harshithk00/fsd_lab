# 1: Hello World

## Setup
```
mkdir exp1_helloworld
cd exp1_helloworld
python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject myproject .
python manage.py startapp myapp
mkdir templates
```

## Settings: Add `'myapp'` to INSTALLED_APPS, set `'DIRS': [BASE_DIR / 'templates']` in TEMPLATES

## myproject/urls.py
```python
from django.urls import path, include
urlpatterns = [path('', include('myapp.urls'))]
```

## myapp/views.py
```python
from django.shortcuts import render
def hello(request):
    return render(request, 'hello.html')
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.hello)]
```

## templates/hello.html
```html
<h1>Hello World</h1>
```

## Run
```
python manage.py runserver
```
http://127.0.0.1:8000/
