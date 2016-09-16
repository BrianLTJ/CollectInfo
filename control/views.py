from django.shortcuts import render
from django.http import HttpResponseRedirect
from info.models import Person
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='admin/login')
def list_index(request):
    people = Person.objects.all()
    return render(request, 'control/index.html', {'people': people})


def login_index(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin')
        else:
            return render(request, 'control/login.html', {'msg': '账户或密码错误'})
    else:
        return render(request, 'control/login.html')
