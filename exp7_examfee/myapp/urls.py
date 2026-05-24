from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('result/', views.result, name='result'),
    path('delete/', views.delete_unpaid, name='delete')]
