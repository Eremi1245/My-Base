from django.shortcuts import render

def state(request):
    title = 'Сотрудники'
    context={
        'title':title,
    }
    return render(request,'clubstate.html',context)