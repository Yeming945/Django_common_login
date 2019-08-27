from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    pass
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')

""" 用户登出后重定向 """
def logout(request):
    pass
    return redirect('/login/')
