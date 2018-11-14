from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='index'),   #首页
    url(r'^login/$',views.login,name='login'), #注册
    url(r'^register/$',views.register,name='register'), #登陆
    url(r'^logout/$',views.logout,name="logout"), #退出登陆
    url(r'^detail/(\d+)/$',views.detail,name='detail'),#商品详情
    url(r'^mycat/$',views.mycat,name='mycat'), #购物车

    url(r'^checkname/$',views.checkname,name='checkname'), #用户名验证


    url(r'^addcart/$',views.addcart,name='addcart'), #添加购物车
    # url(r'subcart/$', views.subcart, name='subcart'),  # 购物车减操作
    url(r'^changecartstatus/$', views.changecartstatus, name='changecartstatus'), # 修改选中状态
    url(r'changecartselect/$', views.changecartselect,name='changecartselect'), # 全选/取消全选

]


