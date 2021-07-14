from django.shortcuts import render

def attestation(request):
    return render(request,'attestation.html')

def attestation_info(request,id):
    return render(request,'attestation_info.html')