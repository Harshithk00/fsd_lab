from django.urls import path
from . import views
urlpatterns = [path('', views.add), path('update/', views.update), path('result/', views.result)]
