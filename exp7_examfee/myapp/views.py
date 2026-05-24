from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            semester=int(request.POST['semester']), fee_paid='fee_paid' in request.POST)
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})

def delete_unpaid(request):
    Student.objects.filter(fee_paid=False).delete()
    return redirect('result')
