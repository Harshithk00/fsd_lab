from django.shortcuts import render, redirect
from .models import Alumni

def add(request):
    if request.method == 'POST':
        Alumni.objects.create(name=request.POST['name'], usn=request.POST['usn'],
            passing_year=int(request.POST['passing_year']), company=request.POST['company'])
        return redirect('result')
    return render(request, 'add.html')

def result(request):
    year = request.GET.get('year', '')
    data = Alumni.objects.filter(passing_year=int(year)) if year else Alumni.objects.none()
    years = Alumni.objects.values_list('passing_year', flat=True).distinct()
    return render(request, 'result.html', {'data': data, 'years': years, 'selected': int(year) if year else 0})
