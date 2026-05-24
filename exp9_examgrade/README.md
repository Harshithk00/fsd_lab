# 9: Exam Grade

## Setup
```
mkdir exp9_examgrade
cd exp9_examgrade
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
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    grade = models.CharField(max_length=2)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            subject=request.POST['subject'], marks=int(request.POST['marks']), grade=request.POST['grade'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Student.objects.filter(grade='O')
    return render(request, 'result.html', {'data': data})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('result/', views.result, name='result')]
```

## templates/add.html
```html
<h2>Add Student</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    USN: <input name="usn"><br>
    Subject: <input name="subject"><br>
    Marks: <input name="marks" type="number"><br>
    Grade: <input name="grade"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">View O Grade</a>
```

## templates/result.html
```html
<h2>Students with O Grade</h2>
<table border="1">
<tr><th>Name</th><th>USN</th><th>Subject</th><th>Marks</th><th>Grade</th></tr>
{% for s in data %}
<tr><td>{{ s.name }}</td><td>{{ s.usn }}</td><td>{{ s.subject }}</td><td>{{ s.marks }}</td><td>{{ s.grade }}</td></tr>
{% endfor %}
</table>
<a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/
