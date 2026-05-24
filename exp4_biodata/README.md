# 4: Biodata Form

## Setup
```
mkdir exp4_biodata
cd exp4_biodata
python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject myproject .
python manage.py startapp myapp
mkdir templates
```

## Settings: Add `'myapp'` to INSTALLED_APPS, set `'DIRS': [BASE_DIR / 'templates']` in TEMPLATES. Add `DATABASES` for sqlite3.

## myproject/urls.py
```python
from django.urls import path, include
urlpatterns = [path('', include('myapp.urls'))]
```

## myapp/models.py
```python
from django.db import models

class Biodata(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
```

## myapp/views.py
```python
from django.shortcuts import render
from .models import Biodata

def biodata(request):
    if request.method == 'POST':
        Biodata.objects.create(
            name=request.POST['name'], age=int(request.POST['age']),
            email=request.POST['email'], phone=request.POST['phone'], address=request.POST['address']
        )
        data = Biodata.objects.all()
        return render(request, 'result.html', {'data': data})
    return render(request, 'form.html')
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.biodata)]
```

## templates/form.html
```html
<h2>Biodata Form</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"><br>
    Age: <input name="age" type="number"><br>
    Email: <input name="email" type="email"><br>
    Phone: <input name="phone"><br>
    Address: <textarea name="address"></textarea><br>
    <button type="submit">Submit</button>
</form>
```

## templates/result.html
```html
<h2>All Biodata Submissions</h2>
<table border="1">
<tr><th>Name</th><th>Age</th><th>Email</th><th>Phone</th><th>Address</th></tr>
{% for b in data %}
<tr><td>{{ b.name }}</td><td>{{ b.age }}</td><td>{{ b.email }}</td><td>{{ b.phone }}</td><td>{{ b.address }}</td></tr>
{% endfor %}
</table>
<br>
<a href="/">Go Back to Form</a>
```

## Run
```
python manage.py makemigrations myapp
python manage.py migrate
python manage.py runserver
```
http://127.0.0.1:8000/
