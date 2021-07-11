from django.urls import path
from .views import state

app_name = 'clubstateapp'

urlpatterns = [
    path('', state, name='index'),
]