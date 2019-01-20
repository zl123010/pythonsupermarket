from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

# 定义登录页面的视图
from user.forms import RegModelForm, LoginModelForm
from user.helper import set_password

from user.models import MarketUsers


class RegView(View):
    def get(self, request):
        return render(request, 'user/reg.html')

    def post(self, request):
        # 接收参数
        data = request.POST
        # 验证数据合法性
        register_form = RegModelForm(data)
        if register_form.is_valid():
            # 操作数据库
            # 获取清洗后的数据
            cleand_data = register_form.cleaned_data
            # 保存
            user = MarketUsers()
            user.phone = cleand_data.get('phone')
            user.password = set_password(cleand_data.get('password'))
            user.save()
            return redirect('user:登录')
        else:
            return render(request, 'user/reg.html', {"form": register_form})


class LoginView(View):
    def get(self, request):
        # 跳转登录页
        return render(request, 'user/login.html')

    def post(self, request):
        # 接受参数
        data = request.POST
        # 验证表单合法
        form = LoginModelForm(data)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = MarketUsers()
            user.phone = cleaned_data.get('phone')
            user.password = set_password(cleaned_data.get('password'))
            user.save()
            return redirect('commodity:主页')
        else:
            return render(request, 'user/login.html', context={'form': form})
