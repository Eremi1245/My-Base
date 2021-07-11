from django.urls import path
from .views import attestation

app_name = 'attestationsapp'

urlpatterns = [
    path('', attestation, name='index'),
]