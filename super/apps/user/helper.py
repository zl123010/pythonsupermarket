from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.profile import region_provider
from django.shortcuts import redirect

from super.settings import SECRET_KEY, ACCESS_KEY_ID, ACCESS_KEY_SECRET
import hashlib
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
import uuid


def set_password(password):
    for _ in range(255):
        pwd_str = "{}{}".format(password, SECRET_KEY)
        h = hashlib.md5(pwd_str.encode('utf-8'))
        password = h.hexdigest()
    return password


def login(request, user):  # 保存session的方法
    request.session['ID'] = user.pk
    request.session['phone'] = user.phone
    request.session['head'] = user.head
    request.session.set_expiry(0)  # 关闭浏览器消失


def check_login(func):  # 验证是否登录的装饰器
    def verify_login(requeset, *args, **kwargs):
        # 验证session中是否有登陆标识
        if requeset.session.get("ID") is None:
            return redirect('user:登录')
        else:
            return func(requeset, *args, **kwargs)

    return verify_login


REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name)

    # 数据提交方式
    # smsRequest.set_method(MT.POST)

    # 数据提交格式
    # smsRequest.set_accept_format(FT.JSON)

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse
