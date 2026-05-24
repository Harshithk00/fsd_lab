# 2: XSS Demo

## Setup
```
mkdir exp2_xss
cd exp2_xss
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

## myapp/views.py
```python
from django.shortcuts import render

def attack(request):
    name = request.POST.get('name', '') if request.method == 'POST' else ''
    return render(request, 'attack.html', {'name': name})

def safe(request):
    name = request.POST.get('name', '') if request.method == 'POST' else ''
    return render(request, 'safe.html', {'name': name})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [
    path('', views.attack),
    path('safe/', views.safe)
]
```

## templates/attack.html
```html
<h2>XSS Attack Page (Vulnerable)</h2>
<form method="POST">
    {% csrf_token %}
    Name: <input name="name">
    <button type="submit">Submit</button>
</form>
<p>Try submitting: &lt;script&gt;alert('Hacked')&lt;/script&gt;</p>
{% if name %}
<h3>Vulnerable Output:</h3>
<p>{{ name|safe }}</p>
{% endif %}
<br>
<a href="/safe/">Go to XSS Safe Page</a>
```

## templates/safe.html
```html
<h2>XSS Safe Page (Auto-escaped)</h2>
<form method="POST">{% csrf_token %}
    Name: <input name="name"> <button type="submit">Submit</button>
</form>
<p>Try submitting: &lt;script&gt;alert('Hacked')&lt;/script&gt;</p>
{% if name %}
<h3>Safe Output:</h3>
<p>{{ name }}</p>
{% endif %}
<br>
<a href="/">Go to XSS Attack Page</a>
```

## Run
```
python manage.py runserver
```
http://127.0.0.1:8000/
