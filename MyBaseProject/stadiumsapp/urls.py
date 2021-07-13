from django.urls import path
from .views import stadium, stad_info

app_name = 'stadiumssapp'

urlpatterns = [
    path('', stadium, name='index'),
    path(r'stad_info<id>', stad_info, name='stad_info'),
]
