from django.conf.urls import url

from user.views import RegView, LoginView, UserView, UserInfoView, SendMeg

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="登录"),
    url(r'^reg/$', RegView.as_view(), name="注册"),
    url(r'^member/$', UserView.as_view(), name='个人中心'),
    url(r'^info/$', UserInfoView.as_view(), name='个人资料'),
    url(r'^senMsg/$', SendMeg.as_view(), name='短信验证')
]
