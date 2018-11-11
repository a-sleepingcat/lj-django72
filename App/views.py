import hashlib
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from App.models import User, Wheel, Goods


# 首页
def index(request):
    #轮播图
    wheels = Wheel.objects.all()

    # 插入商品
    goods = Goods.objects.all()



    data = {
        'wheels' : wheels,
        'username': '',
        'goods':goods,
        'isLogin':''
    }
    #状态保持-获取session
    # username = request.session.get('username')
    #获取token
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        data['username'] = user.username
        data['isLogin'] =1
        return render(request,'index.html', context=data)
    else:
        return render(request,'index.html',context=data)


#加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()



# 注册
def login(request):
    if request.method == 'GET':    #获取注册页面操作
        return render(request,'login.html')
    elif request.method =='POST':   #重客户端获取数据
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.tel = request.POST.get('tel')

        #加密处理
        user.password = generate_password(user.password)

        #随即获取不同的token，使token不唯一，用户名才能覆盖登陆
        user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))

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
        # password = request.POST.get('password')
        # print(username,password)

        #验证，数据库能找到则登陆成功
        password = generate_password(request.POST.get('password'))

            # users = User.objects.filter(username=username, password=password)
        try:
            user = User.objects.get(username=username)
            try:
                user=User.objects.get(username=username,password=password)
                # users.count():  # count（）>0,存在
                # user = users.first()

                # 重定向
                response = redirect('app:index')
                # uuid获取不同的token，用户名才会覆盖
                # user.token = uuid.uuid5(uuid.uuid4(), 'register')
                # 设置cookie
                # response.set_cookie('username',username)
                    # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
                response.set_cookie('token', user.token)
                user.save()
                return response
            except:

                return render(request, 'register.html', context={ 'passwdErr': '密码错误！'})
        except: # 不存在
            return render(request, 'register.html', context={'accountErr': '帐号不存在！'})
        # except:
        #     return render(request, 'register.html', context={'accountErr': '帐号不存在！'})
                # return HttpResponse('用户名或密码错误')
                # return render(request,'register.html')
# 登录
# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         try:
#             user = User.objects.get(username =username )
#             if user.password == generate_password(password):    # 登录成功
#
#                 # 更新token
#                 user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
#                 user.save()
#                 request.session['token'] = user.token
#                 return redirect('axf:mine')
#             else:   # 登录失败
#                 return render(request, 'register.html', context={'passwdErr': '密码错误!'})
#         except:
#             return render(request, 'register.html', context={'usernameErr':'账号不存在!'})




#验证帐号
def checkname(request):
    username = request.GET.get('username')

    responseData ={
        'msg':'帐号可用',
        'status':1,
    }
    print(username)

    user = User.objects.filter(username=username)
    if user.exists():

        responseData['msg'] = '帐号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)

    return JsonResponse(responseData)


#退出登陆
def logout(request):
    response = redirect('app:index')
    #删除token
    response.delete_cookie('token')

    return response



#商品详情
def detail(request,id):
    goods = Goods.objects.all()[int(id)-1]
    print(goods)
    data = {
        'goods':goods,
    }
    return render(request,'detail.html',context=data)

#购物车
def mycat(request):
    return render(request,'mycat.html')

