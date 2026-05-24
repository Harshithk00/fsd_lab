from django.urls import path
from . import views
urlpatterns = [path('', views.add), path('result/', views.result), path('delete/', views.delete)]
