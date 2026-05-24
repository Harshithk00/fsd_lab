# 8: HR Management

## Setup
```
mkdir exp8_hr
cd exp8_hr
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
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_hired = models.DateField()
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Employee

def add(request):
    if request.method == 'POST':
        Employee.objects.create(name=request.POST['name'], email=request.POST['email'],
            phone=request.POST['phone'], date_hired=request.POST['date_hired'],
            job_title=request.POST['job_title'], salary=int(request.POST['salary']))
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Employee.objects.filter(salary__gt=50000)
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
<h2>Add Employee</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    Email: <input name="email" type="email"><br>
    Phone: <input name="phone"><br>
    Date Hired: <input name="date_hired" type="date"><br>
    Job Title: <input name="job_title"><br>
    Salary: <input name="salary" type="number"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">Salary &gt; 50000</a>
```

## templates/result.html
```html
<h2>Employees - Salary &gt; 50000</h2>
<table border="1">
<tr><th>Name</th><th>Email</th><th>Phone</th><th>Hired</th><th>Title</th><th>Salary</th></tr>
{% for e in data %}
<tr><td>{{ e.name }}</td><td>{{ e.email }}</td><td>{{ e.phone }}</td><td>{{ e.date_hired }}</td><td>{{ e.job_title }}</td><td>{{ e.salary }}</td></tr>
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
