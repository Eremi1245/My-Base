from django.urls import path
from .views import stadium

app_name = 'stadiumsapp'

urlpatterns = [
    path('', stadium, name='index'),
]