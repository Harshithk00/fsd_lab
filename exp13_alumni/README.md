# 13: Alumni Tracker

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
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20)
    passing_year = models.IntegerField()
    company = models.CharField(max_length=100)
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Alumni

def add(request):
    if request.method == 'POST':
        Alumni.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            passing_year=int(request.POST['passing_year']), company=request.POST['company'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    year = request.GET.get('year', '')
    data = Alumni.objects.filter(passing_year=int(year)) if year else Alumni.objects.none()
    years = Alumni.objects.values_list('passing_year', flat=True).distinct()
    return render(request, 'result.html', {'data': data, 'years': years, 'selected': int(year) if year else 0})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('result/', views.result, name='result')]
```

## templates/add.html
```html
<h2>Add Alumni</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    USN: <input name="usn"><br>
    Passing Year: <input name="passing_year" type="number"><br>
    Company: <input name="company"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">View Alumni</a>
```

## templates/result.html
```html
<h2>Alumni Tracker</h2>
<form method="GET" action="/result/">
    Year: <select name="year">
        <option value="">--Select--</option>
        {% for y in years %}
        <option value="{{ y }}" {% if y == selected %}selected{% endif %}>{{ y }}</option>
        {% endfor %}
    </select>
    <button type="submit">Filter</button>
</form>
{% if data %}
<table border="1">
<tr><th>Name</th><th>USN</th><th>Year</th><th>Company</th></tr>
{% for a in data %}
<tr><td>{{ a.name }}</td><td>{{ a.usn }}</td><td>{{ a.passing_year }}</td><td>{{ a.company }}</td></tr>
{% endfor %}
</table>
{% endif %}
<a href="/">Add</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/
