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
