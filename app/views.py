
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.shortcuts import render
from app.models import Person
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _, activate
import random








def main(request):
    activate(random.choice(["en", "ru"]))
    return render(request, "comon.html", {"title": _('новости')})






def now_1(request):
    return render(request, "nachalo.html", {})


def now_2(request):
    return render(request, "comon.html", {})


def now_3(request):
    return render(request, "o_nas.html", {})


def now_4(request):
    return render(request, "voto.html", {})

def now_5(request):
    return render(request, "yclygi.html", {})

def now_6(request):
    return render(request, "contact.html", {})



def index(request):
    x = Person.objects.all()
    w = {"z": x, 'w': request.user.is_authenticated}
    if request.user.is_authenticated:
        w['user'] = request.user.username

    return render(request, 'xxx.html', w)


def loging(request):
    user = authenticate(
        username=request.POST['user'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, "error.html", {})
    else:
        login(request, user)
        return HttpResponseRedirect("main_page")


def logout_do(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('main_page')
    else:
        return HttpResponseRedirect('main_page')


def sss_ys(request):
    return render(request, "sss.html", {})


def register(request):
    if request.POST["password"] != request.POST["password2"]:
        return HttpResponse('Пароли не ')
    User.objects.create_user(
        request.POST['login'],
        password=request.POST["password"],

    )
    return HttpResponseRedirect('main_page')


def knop(request):
    resp = {
        "mess": request.POST['a'] + "wor"
    }
    return JsonResponse(resp)