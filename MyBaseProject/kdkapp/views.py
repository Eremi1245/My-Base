from django.shortcuts import render


def kdk(request):
    title = 'КДК'
    context = {
        'title': title,
    }
    return render(request, 'kdk.html', context)


def kdk_info(request, id):
    pass
