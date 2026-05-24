# 5: jQuery Feedback

## Setup
```
mkdir exp5_feedback
cd exp5_feedback
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
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def page(request): 
    return render(request, 'feedback.html')

@csrf_exempt
def submit(request):
    return JsonResponse({'name': request.POST['name'], 'feedback': request.POST['feedback']})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.page), path('submit/', views.submit)]
```

## templates/feedback.html
```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<form id="form">
    Name: <input id="name"> Feedback: <input id="feedback"> <button>Submit</button>
</form>
<div id="list"></div>
<script>
$('#form').submit(function(event){
    event.preventDefault();
    $.post('/submit/', {name: $('#name').val(), feedback: $('#feedback').val()}, function(data){
        $('#list').append('<p>' + data.name + ': ' + data.feedback + '</p>');
    });
});
</script>
```

## Run
```
python manage.py runserver
```
