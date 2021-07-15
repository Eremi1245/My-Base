from django.shortcuts import render


def attestation(request):
    title = 'Аттестация'
    context = {
        'title': title,
    }
    return render(request, 'attestation.html', context)


def attestation_info(request, id):
    return render(request, 'attestation_info.html')
