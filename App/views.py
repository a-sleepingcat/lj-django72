from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from App.models import User


def index(request):
    #状态保持-获取session
    # username = request.session.get('username')
    #获取token
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        return render(request,'index.html',context={'username':user.username})
    else:
        return render(request,'index.html')




def login(request):
    if request.method == 'GET':    #获取注册页面操作
        return render(request,'login.html')
    elif request.method =='POST':   #重客户端获取数据
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.tel = request.POST.get('tel')

        #存入数据库
        user.save()

        #重定向
        response = redirect('app:index')

        #状态保持

        response.set_cookie('token',user.token)
        return response
