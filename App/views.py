import hashlib
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页
from App.models import User, Wheel, Goods, Cart


# 首页
def index(request):
    # 轮播图
    wheels = Wheel.objects.all()

    # 插入商品
    goods = Goods.objects.all()

    data = {
        'wheels': wheels,
        'username': '',
        'goods': goods,
        'isLogin': ''
    }
    # 状态保持-获取session
    # username = request.session.get('username')
    # 获取token
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    if users.exists():
        user = users.first()
        data['username'] = user.username
        data['isLogin'] = 1
        return render(request, 'index.html', context=data)
    else:
        return render(request, 'index.html', context=data)


# 加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 注册
def login(request):
    if request.method == 'GET':  # 获取注册页面操作
        return render(request, 'login.html')
    elif request.method == 'POST':  # 重客户端获取数据
        user = User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.tel = request.POST.get('tel')

        # 加密处理
        user.password = generate_password(user.password)

        # 随即获取不同的token，使token不唯一，用户名才能覆盖登陆
        user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))

        # 存入数据库
        user.save()

        # 重定向
        response = redirect('app:index')

        # 状态保持

        response.set_cookie('token', user.token)
        return response


# 登陆
def register(request):
    if request.method == 'GET':  # 获取方式
        return render(request, 'register.html')  # 返回登陆页面
    elif request.method == 'POST':  # 获取登陆方式
        # 获取数据
        username = request.POST.get('username')
        # password = request.POST.get('password')
        # print(username,password)

        # 验证，数据库能找到则登陆成功
        password = generate_password(request.POST.get('password'))

        # users = User.objects.filter(username=username, password=password)
        try:
            user = User.objects.get(username=username)
            try:
                user = User.objects.get(username=username, password=password)
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

                return render(request, 'register.html', context={'passwdErr': '密码错误！'})
        except:  # 不存在
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


# 验证帐号

# 帐号验证
def checkname(request):
    username = request.GET.get('username')

    responseData = {
        'msg': '帐号可用',
        'status': 1,
    }
    print(username)

    user = User.objects.filter(username=username)
    if user.exists():
        responseData['msg'] = '帐号已被占用'
        responseData['status'] = -1
        return JsonResponse(responseData)

    return JsonResponse(responseData)


# 退出登陆
def logout(request):
    response = redirect('app:index')
    # 删除token
    response.delete_cookie('token')

    return response


# 商品详情
def detail(request, id):
    # goods = Goods.objects.all()[int(id)-1]
    goods = Goods.objects.filter(id=id).all().first()
    # 购物车数据
    token = request.COOKIES.get('token')
    # user = User.objects.get(token=token)
    carts = []

    if token:  # 根据用户，获取对应用户下所有购物车数据
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user)

    data = {
        'goods': goods,
        'carts': carts,
        'token': token,
        'user':  user,
    }
    return render(request, 'detail.html', context=data)


# 购物车
def mycat(request):
    token = request.COOKIES.get('token')
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)
        return render(request, 'mycat.html', context={'carts': carts})
    else:  # 跳转到登陆页面
      return redirect('app:register')
# return render(request,'mycat.html')

# 加操作
def addcart(request):
    goodsid = request.GET.get('goodsid')
    num = request.GET.get('num')
    # print(goodsid,num)
    token = request.COOKIES.get('token')
    responseData = {
        'msg': '添加购物车成功',
        'status': 1  # 1标识添加成功，0标识添加失败，-1标识未登陆

    }
    if token:  # 登陆[直接操作模型]
        # 获取用户
        user = User.objects.get(token=token)
        # 获取商品
        goods = Goods.objects.get(pk=goodsid)
        # 商品已经在购物车，只改商品个数
        # 商品不存在购物车，新建对象（加入一条新的数据）
        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():  # 修改数量
            cart = carts.first()
            cart.number = int(cart.number) + int(num)
            cart.save()
            responseData['number'] = cart.number
        else:  # 添加一条新记录
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = num
            cart.save()
            responseData['number'] = cart.number
        return JsonResponse(responseData)
    else:  # 未登录[跳转到登陆页面]
        responseData['msg'] = '未登录，请登录后操作'
        responseData['status'] = -1
        return JsonResponse(responseData)



# def subcart(request):
#     token = request.COOKIES.get('token')
#     goodsid = request.GET.get('goodsid')
#     print(goodsid)
#     # 显示减号肯定的是登陆了，不要判断了
#     # 对应用户和商品
#     user = User.objects.get(token=token)
#     goods = Goods.objects.get(pk=goodsid)
#
#     # 删减操作
#     cart = Cart.objects.filter(user=user).filter(goods=goods).first()
#     cart.number = cart.number - 1
#     cart.save()
#
#     responseData = {
#         'mag': '购物车减操作成功',
#         'status': 1,
#         'number': cart.number
#     }
#
#     return JsonResponse(responseData)


# 修改选中状态
def changecartstatus(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    responseData = {
        'msg': '选中状态改变',
        'status': 1,
        'isselect': cart.isselect
    }

    return JsonResponse(responseData)


# 全选/取消全选
def changecartselect(request):
    isselect = request.GET.get('isselect')
    if isselect == 'true':
        isselect = True
    else:
        isselect = False
