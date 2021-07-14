from django.urls import path
from .views import attestation,attestation_info

app_name = 'attestationsapp'

urlpatterns = [
    path('attestation', attestation, name='index'),
    path('attestation_info<id>', attestation_info, name='at_info'),
]