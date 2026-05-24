from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            department=request.POST['department'], grade=request.POST['grade'])
        return redirect('result')
    return render(request, 'add.html')

def update(request):
    msg = ''
    if request.method == 'POST':
        count = Student.objects.filter(name=request.POST['name']).update(grade=request.POST['grade'])
        msg = f'Updated {count} record(s)' if count else 'Not found'
    return render(request, 'update.html', {'msg': msg})

def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})
