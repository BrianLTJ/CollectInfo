from django.shortcuts import render
from info.models import Person

# Create your views here.
def index(request):
    return render(request, 'info/index.html')


def add_handler(request):
    if request.method == 'POST':
        p = Person()
        p.name = request.POST.get('name')
        p.qq = request.POST.get('qq')
        p.phone = request.POST.get('phone')
        p.dorm = request.POST.get('dorm')
        p.birthday = request.POST.get('birthday')
        p.place = request.POST.get('place')
        p.save()

        return render(request, 'info/result.html', {'result': 'ok'})
    else:
        return render(request, 'info/result.html', {'result': 'error'})
