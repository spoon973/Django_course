from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 首页index试图函数路径url
    url(r'^index1$', views.index, name='index'),
    # 测试错误html文件路径
    url(r'^index2$', views.index2),
    # 模板变量
    url(r'^temp_var$', views.temp_var),
    # 模板标签
    url(r'^temp_tages$', views.temp_tages),
    # 模板过滤器
    url(r'^temp_filter$', views.temp_filter),
    # 模板继承
    url(r'^temp_inherit$', views.temp_inherit),
    # html转义
    url(r'^html_escape$', views.html_escape),
    # 登录视图
    url(r'^login$', views.login),
    # 进行登录验证
    url(r'^login_check$', views.login_check),
    # 修改密码页面显示
    url(r'^change_pwd$', views.change_pwd),
    # 修改密码处理
    url(r'^change_pwd_action$', views.change_pwd_action),
    # 产生验证码图片
    url(r'^verify_code$', views.verify_code),
    # url反向解析页面
    url(r'^url_reverse$', views.url_reverse),
    # 捕获位置参数
    url(r'^show_args/(\d+)/(\d+)', views.show_args, name='show_args'),
    # 捕获关键字参数
    url(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs, name='show_kwargs'),
]
