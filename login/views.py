from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from. import models


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容'
        if username.strip() and password:  # 确保用户名密码不为空
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在!'
                return render(request, 'login/login.html', {'message': message})
            if user.password == password:
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确!'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message':message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


""" 用户登出后重定向 """


def logout(request):
    pass
    return redirect('/login/')
