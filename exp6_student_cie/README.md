# 6: Student CIE

## Setup
```
mkdir exp6_student_cie
cd exp6_student_cie
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
    sub_code = models.CharField(max_length=20)
    cie_marks = models.IntegerField()
```

## myapp/views.py
```python
from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(usn=request.POST['usn'], name=request.POST['name'],
            sub_code=request.POST['sub_code'], cie_marks=int(request.POST['cie_marks']))
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Student.objects.filter(cie_marks__lt=20)
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
    USN: <input name="usn"><br>
    Name: <input name="name"><br>
    Subject Code: <input name="sub_code"><br>
    CIE Marks: <input name="cie_marks" type="number"><br>
    <button type="submit">Submit</button>
</form>
<a href="/result/">View CIE &lt; 20</a>
```

## templates/result.html
```html
<h2>Students with CIE &lt; 20</h2>
<table border="1">
<tr><th>USN</th><th>Name</th><th>Subject</th><th>CIE</th></tr>
{% for s in data %}
<tr><td>{{ s.usn }}</td><td>{{ s.name }}</td><td>{{ s.sub_code }}</td><td>{{ s.cie_marks }}</td></tr>
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
