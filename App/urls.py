from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$',views.index,name='index'),   #首页
    url(r'^login/$',views.login,name='login')  #注册
]

