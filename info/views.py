from django.shortcuts import render
from info.models import Person

# Create your views here.
def index(request):
    return render(request, 'info/index.html', {'type': 'new'})


def add_handler(request):
    if request.method == 'POST':
        p = Person()
        p.name = request.POST.get('name')
        p.qq = request.POST.get('qq')
        p.classname = request.POST.get('classname')
        p.phone = request.POST.get('phone')
        p.dorm = request.POST.get('dorm')
        p.birthday = request.POST.get('birthday')
        p.place = request.POST.get('place')
        p.height = request.POST.get('height')
        p.sex = request.POST.get('sex')
        p.weight = request.POST.get('weight')
        p.size = request.POST.get('size')
        p.save()

        return render(request, 'info/result.html', {'result': 'ok'})
    else:
        return render(request, 'info/result.html', {'result': 'error'})


def edit_index(request):
    opt_result = False
    p = Person.objects.all()
    if request.method == 'POST':
        p = p.filter(phone=request.POST.get('phone'))
        p = p.filter(name=request.POST.get('name'))
        if len(p) != 1:
            opt_result = False
            print("Error person: len=" + str(len(p)))
        else:
            opt_result = True
    else:
        opt_result = False

    if opt_result:
        return render(request, 'info/index.html', {'type': 'edit', 'p': p[0]})
    else:
        return render(request, 'info/result.html', {'result': 'error'})


def edit_handler(request):
    opt_result = False
    if request.method == 'POST':
        p = Person.objects.filter(id=request.POST.get('id'))
        if len(p) != 1:
            opt_result = False
        else:
            p = p[0]
            p.qq = request.POST.get('qq')
            p.dorm = request.POST.get('dorm')
            p.classname = request.POST.get('classname')
            p.birthday = request.POST.get('birthday')
            p.place = request.POST.get('place')
            p.height = request.POST.get('height')
            p.sex = request.POST.get('sex')
            p.weight = request.POST.get('weight')
            p.size = request.POST.get('size')
            p.save()

            opt_result = True
    else:
        opt_result = False

    if opt_result:
        return render(request, 'info/result.html', {'result': 'ok'})
    else:
        return render(request, 'info/result.html', {'result': 'error'})



