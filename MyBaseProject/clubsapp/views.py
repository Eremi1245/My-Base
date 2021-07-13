from django.shortcuts import render

from .models import Clubs


def club(request):
    title = 'клубы'
    clubs = Clubs.objects.all()
    context = {
        'title': title,
        'clubs': clubs,
    }
    return render(request, 'stadium.html', context)


class Counter:
    def __init__(self):
        self.now = 1

    def plus(self):
        self.now = self.now+1
        return ''


def club_info(request, id):
    club = Clubs.objects.get(pk=id)
    title = club.shrt_name
    club_inf = {}
    for field in club._meta.fields[:-2]:
        if field.name != 'avatar':
            club_inf[field.name] = club.__dict__[field.name]
    count = Counter()
    context = {
        'title': title,
        'club': club_inf,
        'count': count,
    }
    return render(request,
                  'stad_info.html',
                  context
                  )
