from django.urls import path
from .views import kdk

app_name = 'kdkapp'

urlpatterns = [
    path('', kdk, name='index'),
]