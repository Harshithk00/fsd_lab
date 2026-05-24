from django.shortcuts import render, redirect
from .models import Student

def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            subject=request.POST['subject'], marks=int(request.POST['marks']), grade=request.POST['grade'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    data = Student.objects.filter(grade='O')
    return render(request, 'result.html', {'data': data})
