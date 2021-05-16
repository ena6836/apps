from django.urls import path
from . import views

app_name = 'oekaki'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
]