from django.urls import path
from . import views
urlpatterns = [path('', views.add, name='add'), path('update/', views.update, name='update'),
    path('result/', views.result, name='result')]
