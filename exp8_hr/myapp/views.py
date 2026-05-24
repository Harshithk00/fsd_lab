from django.shortcuts import render, redirect
from .models import Employee

def add(request):
    if request.method == 'POST':
        Employee.objects.create(name=request.POST['name'], email=request.POST['email'],
            phone=request.POST['phone'], date_hired=request.POST['date_hired'],
            job_title=request.POST['job_title'], salary=int(request.POST['salary']))
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Employee.objects.filter(salary__gt=50000)
    return render(request, 'result.html', {'data': data})
