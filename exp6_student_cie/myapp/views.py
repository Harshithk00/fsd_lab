from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(usn=request.POST['usn'], name=request.POST['name'], sub=request.POST['sub'], cie=request.POST['cie'])
        return redirect('/result/')
    return render(request, 'add.html')

def result(request):
    return render(request, 'result.html', {'data': Student.objects.filter(cie__lt=20)})
