import random

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

# 定义登录页面的视图
from user.forms import RegModelForm, LoginModelForm
from user.helper import set_password, login, check_login
import re
from user.models import MarketUsers
from django_redis import get_redis_connection


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

            user = form.cleaned_data['user']
            login(request, user)

            return redirect('user:个人中心')
        else:
            return render(request, 'user/login.html', context={'form': form})


class UserView(View):
    # @method_decorator(check_login)
    def get(self, request):
        return render(request, 'user/member.html')

    # @method_decorator(check_login)
    def post(self, request):
        pass


class UserInfoView(View):
    def get(self, request):
        userinfo = MarketUsers.objects.get(pk=id)
        context = {
            'userinfo': userinfo
        }
        return render(request, 'user/infor.html', context=context)

    def post(self, request):
        data = request.POST
        id = data.get('id')
        MarketUsers.objects.filter(id=id).update(**data)
        return redirect('user:个人资料', id)


class SendMeg(View):
    def get(self, request):
        pass

    def post(self, request):
        # 接受参数
        phone = request.POST.get('phone', '')
        rs = re.search('^1[3-9]\d{9}$', phone)
        # 判断参数合法性 如果合法返回一个对象不合法返回None
        if rs is None:
            return JsonResponse({'error': 1, 'errmsg': '手机号码格式不正确'})
        # 操作数据
        # 生成随机验证码进行模拟验证
        random_code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        print("随机验证码为{}".format(random_code))
        # 保存验证码到redis中
        r = get_redis_connection()
        # 保存手机号对应的验证码
        r.set(phone, random_code)
        # 设置10分钟后过期
        r.expire(phone, 600)
        # 获取手机号发送验证码的次数
        code_times = "{}_times".format(phone)
        now_time = r.get(code_times)
        if now_time is None or now_time < 5:
            # 发送验证码次数不存在或小于5
            r.incr(code_times)
            # 设置10分钟后过期
            r.expire(code_times, 600)
        else:
            # 返回错误 告知用户验证码发送次数过多
            return JsonResponse({"error": 1, "errmsg": "验证码发送次数过多"})

        # 合成响应

        return JsonResponse({'error': 0})
