# 10: Placement

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
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(usn=request.POST['usn'], name=request.POST['name'], company=request.POST['company'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Student.objects.filter(company='Amazon')
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
<h2>Add Placement</h2>
<form method="POST">{% csrf_token %}
    USN: <input name="usn"><br>
    Name: <input name="name"><br>
    Company: <input name="company"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">Amazon Placements</a>
```

## templates/result.html
```html
<h2>Students Placed in Amazon</h2>
<table border="1">
<tr><th>USN</th><th>Name</th><th>Company</th></tr>
{% for s in data %}
<tr><td>{{ s.usn }}</td><td>{{ s.name }}</td><td>{{ s.company }}</td></tr>
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
