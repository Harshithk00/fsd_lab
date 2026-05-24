from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def page(request): 
    return render(request, 'feedback.html')

@csrf_exempt
def submit(request):
    return JsonResponse({'name': request.POST['name'], 'feedback': request.POST['feedback']})
