from django.urls import path
from . import views

urlpatterns = [
    path('', views.attack, name='attack'),
    path('safe/', views.safe, name='safe')
]
