# 12: Grade Update

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
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    grade = models.CharField(max_length=2)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            department=request.POST['department'], grade=request.POST['grade'])
        return redirect('result')
    return render(request, 'add.html')

def update(request):
    msg = ''
    if request.method == 'POST':
        count = Student.objects.filter(name=request.POST['name']).update(grade=request.POST['grade'])
        msg = f'Updated {count} record(s)' if count else 'Not found'
    return render(request, 'update.html', {'msg': msg})

def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('update/', views.update, name='update'),
    path('result/', views.result, name='result')]
```

## templates/add.html
```html
<h2>Add Student</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    USN: <input name="usn"><br>
    Department: <input name="department"><br>
    Grade: <input name="grade"><br>
    <button type="submit">Submit</button>
</form>
<a href="/update/">Update Grade</a> | <a href="/result/">View All</a>
```

## templates/update.html
```html
<h2>Update Grade</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    New Grade: <input name="grade"><br>
    <button type="submit">Update</button>
</form>
{% if msg %}<p>{{ msg }}</p>{% endif %}
<a href="/">Add</a> | <a href="/result/">View All</a>
```

## templates/result.html
```html
<h2>All Students</h2>
<table border="1">
<tr><th>Name</th><th>USN</th><th>Dept</th><th>Grade</th></tr>
{% for s in data %}
<tr><td>{{ s.name }}</td><td>{{ s.usn }}</td><td>{{ s.department }}</td><td>{{ s.grade }}</td></tr>
{% endfor %}
</table>
<a href="/">Add</a> | <a href="/update/">Update</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/
