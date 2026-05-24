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
