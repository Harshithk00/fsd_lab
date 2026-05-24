# 11: Faculty

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
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Faculty

def add(request):
    if request.method == 'POST':
        Faculty.objects.create(fid=request.POST['fid'], title=request.POST['title'],
            name=request.POST['name'], branch=request.POST['branch'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Faculty.objects.filter(branch='CSE', title='Professor')
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
<h2>Add Faculty</h2>
<form method="POST">{% csrf_token %}
    ID: <input name="fid"><br>
    Title: <input name="title"><br>
    Name: <input name="name"><br>
    Branch: <input name="branch"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">CSE Professors</a>
```

## templates/result.html
```html
<h2>CSE Professors</h2>
<table border="1">
<tr><th>ID</th><th>Title</th><th>Name</th><th>Branch</th></tr>
{% for f in data %}
<tr><td>{{ f.fid }}</td><td>{{ f.title }}</td><td>{{ f.name }}</td><td>{{ f.branch }}</td></tr>
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
