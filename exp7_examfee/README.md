# 7

## Setup
```
mkdir exp7_examfee
cd exp7_examfee
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
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    sem = models.IntegerField()
    fee = models.BooleanField(default=False)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student
def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'], sem=request.POST['sem'], fee='fee' in request.POST)
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})
def delete(request):
    Student.objects.filter(fee=False).delete()
    return redirect('/result/')
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add), path('result/', views.result), path('delete/', views.delete)]
```

## templates/add.html
```html
<form method="POST">{% csrf_token %}
 Name:<input name="name"> USN:<input name="usn"> Sem:<input name="sem"> Fee:<input name="fee" type="checkbox"> <button>Add</button>
</form><a href="/result/">View</a>
```

## templates/result.html
```html
<table border="1"><tr><th>Name</th><th>USN</th><th>Sem</th><th>Fee</th></tr>
{% for s in data %}<tr><td>{{s.name}}</td><td>{{s.usn}}</td><td>{{s.sem}}</td><td>{{s.fee|yesno:"Y,N"}}</td></tr>{% endfor %}</table>
<a href="/delete/">Del Unpaid</a> | <a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
