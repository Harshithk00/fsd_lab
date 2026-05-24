from django.shortcuts import render

def attack(request):
    name = request.POST.get('name', '') if request.method == 'POST' else ''
    return render(request, 'attack.html', {'name': name})

def safe(request):
    name = request.POST.get('name', '') if request.method == 'POST' else ''
    return render(request, 'safe.html', {'name': name})
