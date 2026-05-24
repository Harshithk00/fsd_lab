# 3: Weather App

## Setup
```
mkdir exp3_weather
cd exp3_weather
python -m venv venv
venv\Scripts\activate
pip install django requests
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
import requests
from django.shortcuts import render

def weather(request):
    data, error = {}, ''
    if request.method == 'POST':
        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'
        res = requests.get(url).json()
        if res.get('cod') == 200:
            data = {'city': res['name'], 'temp': res['main']['temp'], 'desc': res['weather'][0]['description']}
        else:
            error = 'City not found!'
    return render(request, 'weather.html', {'data': data, 'error': error})
```

## myapp/urls.py
```python
from django.urls import path
from . import views
urlpatterns = [path('', views.weather)]
```

## templates/weather.html
```html
<h2>Weather App</h2>
<form method="POST">{% csrf_token %}
    City: <input name="city"> <button type="submit">Get Weather</button>
</form>
{% if error %}<p>{{ error }}</p>{% endif %}
{% if data %}
<p>City: {{ data.city }}</p>
<p>Temp: {{ data.temp }} C</p>
<p>Desc: {{ data.desc }}</p>
{% endif %}
```

## Run
```
python manage.py runserver
```
http://127.0.0.1:8000/
