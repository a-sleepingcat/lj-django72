import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from App.models import User

# 首页
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



# 注册
def login(request):
    if request.method == 'GET':    #获取注册页面操作
        return render(request,'login.html')
    elif request.method =='POST':   #重客户端获取数据
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.tel = request.POST.get('tel')
        user.token = uuid.uuid5(uuid.uuid4(), 'login')

        #存入数据库
        user.save()

        #重定向
        response = redirect('app:index')

        #状态保持

        response.set_cookie('token',user.token)
        return response


# 登陆
def register(request):
    if request.method =='GET': #获取方式
        return render(request,'register.html') #返回登陆页面
    elif request.method =='POST': #获取登陆方式
        # 获取数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        #验证，数据库能找到则登陆成功
        users = User.objects.filter(username=username,password=password)
        if users.count(): #count（）>0,存在
            user = users.first()

            #重定向
            response = redirect('app:index')
            #设置cookie
            # response.set_cookie('username',username)
            user.token = uuid.uuid5(uuid.uuid4(), 'register')
            response.set_cookie('token', user.token)
            user.save()
            return response
        else: #不存在
            return HttpResponse('用户名或密码错误')


def logout(request):
    response = redirect('app:index')
    response.delete_cookie('token')

    return response