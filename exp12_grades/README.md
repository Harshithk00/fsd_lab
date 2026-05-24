# 12

## Setup
```
mkdir exp12_grades
cd exp12_grades
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
    dept = models.CharField(max_length=50)
    grade = models.CharField(max_length=2)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student
def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'], dept=request.POST['dept'], grade=request.POST['grade'])
        return redirect('/result/')
    return render(request, 'add.html')
def update(request):
    m = ''
    if request.method == 'POST': m = "Updated" if Student.objects.filter(name=request.POST['name']).update(grade=request.POST['grade']) else "Not found"
    return render(request, 'update.html', {'m': m})
def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add), path('update/', views.update), path('result/', views.result)]
```

## templates/add.html
```html
<form method="POST">{% csrf_token %}
 Name:<input name="name"> USN:<input name="usn"> Dept:<input name="dept"> Grade:<input name="grade"> <button>Add</button>
</form><a href="/update/">Update</a> | <a href="/result/">View All</a>
```

## templates/update.html
```html
<form method="POST">{% csrf_token %}
 Name:<input name="name"> New Grade:<input name="grade"> <button>Update</button>
</form>{{m}}<br><a href="/">Add</a> | <a href="/result/">View</a>
```

## templates/result.html
```html
<table border="1"><tr><th>Name</th><th>USN</th><th>Dept</th><th>Grade</th></tr>
{% for s in data %}<tr><td>{{s.name}}</td><td>{{s.usn}}</td><td>{{s.dept}}</td><td>{{s.grade}}</td></tr>{% endfor %}</table><a href="/">Add</a> | <a href="/update/">Update</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
