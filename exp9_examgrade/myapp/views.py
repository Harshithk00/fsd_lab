from django.shortcuts import render, redirect
from .models import Student
def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'], sub=request.POST['sub'], marks=request.POST['marks'], grade=request.POST['grade'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Student.objects.filter(grade='O')})
