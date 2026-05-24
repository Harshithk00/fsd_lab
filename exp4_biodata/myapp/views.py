from django.shortcuts import render
from .models import Biodata

def biodata(request):
    if request.method == 'POST':
        # Save to DB
        Biodata.objects.create(
            name=request.POST['name'],
            age=int(request.POST['age']),
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address']
        )
        data = Biodata.objects.all()
        return render(request, 'result.html', {'data': data})
    return render(request, 'form.html')
