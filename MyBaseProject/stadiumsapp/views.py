from django.shortcuts import render

from .models import Stadiums


def stadium(request):
    title = 'стадионы'
    stadiums = Stadiums.objects.all()
    context = {
        'title': title,
        'stadiums': stadiums,
    }
    return render(request,'stadium.html',context)

def stad_info(request,id):
    return render(request,'stad_info.html')