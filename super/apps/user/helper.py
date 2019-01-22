from django.shortcuts import redirect

from super.settings import SECRET_KEY
import hashlib


def set_password(password):
    for _ in range(255):
        pwd_str = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pwd_str.encode('utf-8'))
        password = h.hexdigest()
    return password


def login(request, user):  # 保存session的方法
    request.session['ID'] = user.pk
    request.session['phone'] = user.phone
    request.session.set_expiry(0)  # 关闭浏览器消失


def check_login(func):  # 验证是否登录的装饰器
    def verify_login(requeset, *args, **kwargs):
        # 验证session中是否有登陆标识
        if requeset.session.get("ID") is None:
            return redirect('user:登录')
        else:
            return func(requeset, *args, **kwargs)

    return verify_login
