from django.shortcuts import render, redirect
from .models import Student
def add(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['name'], usn=request.POST['usn'], dept=request.POST['dept'], grade=request.POST['grade'])
        return redirect('/result/')
    return render(request, 'add.html')
def update(request):
    m = ''
    if request.method == 'POST': m = "Updated" if Student.objects.filter(name=request.POST['name']).update(grade=request.POST['grade']) else "Not found"
    return render(request, 'update.html', {'m': m})
def result(request):
    return render(request, 'result.html', {'data': Student.objects.all()})
