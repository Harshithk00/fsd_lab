# 8

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
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    job = models.CharField(max_length=50)
    sal = models.IntegerField()
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Employee
def add(request):
    if request.method == 'POST':
        Employee.objects.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], date=request.POST['date'], job=request.POST['job'], sal=request.POST['sal'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Employee.objects.filter(sal__gt=50000)})
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
 Name:<input name="name"> Email:<input name="email"> Phone:<input name="phone"> Date:<input name="date" type="date"> Job:<input name="job"> Sal:<input name="sal"> <button>Add</button>
</form><a href="/result/">View Sal>50k</a>
```

## templates/result.html
```html
<table border="1"><tr><th>Name</th><th>Email</th><th>Phone</th><th>Date</th><th>Job</th><th>Sal</th></tr>
{% for e in data %}<tr><td>{{e.name}}</td><td>{{e.email}}</td><td>{{e.phone}}</td><td>{{e.date}}</td><td>{{e.job}}</td><td>{{e.sal}}</td></tr>{% endfor %}</table><a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
