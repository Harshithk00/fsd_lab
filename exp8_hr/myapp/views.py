from django.shortcuts import render, redirect
from .models import Employee
def add(request):
    if request.method == 'POST':
        Employee.objects.create(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'], date=request.POST['date'], job=request.POST['job'], sal=request.POST['sal'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Employee.objects.filter(sal__gt=50000)})
