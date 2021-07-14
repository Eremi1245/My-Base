from django.urls import path
from .views import kdk,kdk_info

app_name = 'kdkapp'

urlpatterns = [
    path('', kdk, name='index'),
    path('kdk_info<id>',kdk_info,name='kdk_info')
]