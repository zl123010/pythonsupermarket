from django.conf.urls import url

from user.views import RegView, LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="登录"),
    url(r'^reg/$', RegView.as_view(), name="注册")
]
