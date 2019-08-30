from .import forms
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from. import models


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在!'
                return render(request, 'login/login.html', locals())
            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确!'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


""" 用户登出后重定向 """


def logout(request):
    pass
    return redirect('/login/')
