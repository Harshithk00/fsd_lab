# 10

## Setup
```
mkdir exp10_placement
cd exp10_placement
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
class Student(models.Model):
    usn = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student
def add(request):
    if request.method == 'POST':
        Student.objects.create(usn=request.POST['usn'], name=request.POST['name'], company=request.POST['company'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Student.objects.filter(company='Amazon')})
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
 USN:<input name="usn"> Name:<input name="name"> Company:<input name="company"> <button>Add</button>
</form><a href="/result/">View Amazon</a>
```

## templates/result.html
```html
<table border="1"><tr><th>USN</th><th>Name</th><th>Company</th></tr>
{% for s in data %}<tr><td>{{s.usn}}</td><td>{{s.name}}</td><td>{{s.company}}</td></tr>{% endfor %}</table><a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
