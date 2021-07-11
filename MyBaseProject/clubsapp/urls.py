from django.urls import path
from .views import club

app_name = 'clubsapp'

urlpatterns = [
    path('', club, name='index'),
]