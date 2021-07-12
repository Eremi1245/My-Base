from django.urls import path
from .views import club,club_info

app_name = 'clubsapp'

urlpatterns = [
    path('', club, name='index'),
    path('club_info',club_info,name='club_info'),
]