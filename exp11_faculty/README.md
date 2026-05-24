# 11

## Setup
```
mkdir exp11_faculty
cd exp11_faculty
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

## myapp/models.py
```python
from django.db import models
class Faculty(models.Model):
    fid = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Faculty
def add(request):
    if request.method == 'POST':
        Faculty.objects.create(fid=request.POST['fid'], title=request.POST['title'], name=request.POST['name'], branch=request.POST['branch'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Faculty.objects.filter(branch='CSE', title='Professor')})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add), path('result/', views.result)]
```

## templates/add.html
```html
<form method="POST">{% csrf_token %}
 ID:<input name="fid"> Title:<input name="title"> Name:<input name="name"> Branch:<input name="branch"> <button>Add</button>
</form><a href="/result/">View CSE Profs</a>
```

## templates/result.html
```html
<table border="1"><tr><th>ID</th><th>Title</th><th>Name</th><th>Branch</th></tr>
{% for f in data %}<tr><td>{{f.fid}}</td><td>{{f.title}}</td><td>{{f.name}}</td><td>{{f.branch}}</td></tr>{% endfor %}</table><a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
