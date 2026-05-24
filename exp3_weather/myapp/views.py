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
