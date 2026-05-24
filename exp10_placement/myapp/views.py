from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(usn=request.POST['usn'], name=request.POST['name'], company=request.POST['company'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Student.objects.filter(company='Amazon')
    return render(request, 'result.html', {'data': data})
