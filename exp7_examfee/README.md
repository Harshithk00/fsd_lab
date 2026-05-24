# 7: Exam Fee

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
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    semester = models.IntegerField()
    fee_paid = models.BooleanField(default=False)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            semester=int(request.POST['semester']), fee_paid='fee_paid' in request.POST)
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})

def delete_unpaid(request):
    Student.objects.filter(fee_paid=False).delete()
    return redirect('result')
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('result/', views.result, name='result'),
    path('delete/', views.delete_unpaid, name='delete')]
```

## templates/add.html
```html
<h2>Add Student - Exam Fee</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    USN: <input name="usn"><br>
    Semester: <input name="semester" type="number"><br>
    Fee Paid: <input name="fee_paid" type="checkbox"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">View All</a>
```

## templates/result.html
```html
<h2>All Students</h2>
<table border="1">
<tr><th>Name</th><th>USN</th><th>Sem</th><th>Fee</th></tr>
{% for s in data %}
<tr><td>{{ s.name }}</td><td>{{ s.usn }}</td><td>{{ s.semester }}</td><td>{{ s.fee_paid|yesno:"Yes,No" }}</td></tr>
{% endfor %}
</table>
<a href="/delete/">Delete Unpaid</a> | <a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/
