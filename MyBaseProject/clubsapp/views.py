from django.shortcuts import render

from .models import Clubs


def club(request):
    title = 'клубы'
    clubs = Clubs.objects.all()
    context = {
        'title':title,
        'clubs':clubs,
    }
    return render(request,'club.html',context)


def club_info(request):
    return render(request,'club_info.html')