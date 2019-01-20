from django.conf.urls import url

from user.views import UserView, RegView

urlpatterns = [
    url(r'^login/$', UserView.as_view(), name="登录"),
    url(r'^reg/$', RegView.as_view(), name="注册")
]
