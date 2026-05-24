from django.shortcuts import render, redirect
from .models import Faculty
def add(request):
    if request.method == 'POST':
        Faculty.objects.create(fid=request.POST['fid'], title=request.POST['title'], name=request.POST['name'], branch=request.POST['branch'])
        return redirect('/result/')
    return render(request, 'add.html')
def result(request):
    return render(request, 'result.html', {'data': Faculty.objects.filter(branch='CSE', title='Professor')})
