# 13

## Setup
```
mkdir exp13_alumni
cd exp13_alumni
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
class Alumni(models.Model):
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=20)
    year = models.IntegerField()
    company = models.CharField(max_length=50)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Alumni
def add(request):
    if request.method == 'POST':
        Alumni.objects.create(name=request.POST['name'], usn=request.POST['usn'], year=request.POST['year'], company=request.POST['company'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    y = request.GET.get('year')
    return render(request, 'result.html', {'data': Alumni.objects.filter(year=y) if y else None})
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
 Name:<input name="name"> USN:<input name="usn"> Year:<input name="year"> Company:<input name="company"> <button>Add</button>
</form><a href="/result/">View</a>
```

## templates/result.html
```html
<form method="GET" action="/result/">Year: <input name="year"> <button>Filter</button></form>
{% if data %}<table border="1"><tr><th>Name</th><th>USN</th><th>Year</th><th>Company</th></tr>
{% for a in data %}<tr><td>{{a.name}}</td><td>{{a.usn}}</td><td>{{a.year}}</td><td>{{a.company}}</td></tr>{% endfor %}</table>{% endif %}
<a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
