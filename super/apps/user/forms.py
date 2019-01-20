from django import forms

from user.helper import set_password
from user.models import MarketUsers


class RegModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码未填写',
                                   'max_length': '密码长度不能大于16个字符',
                                   'min_length': '密码长度不能小于6个字符'
                               })
    repassword = forms.CharField(error_messages={
        'required': '确认密码未填写'
    })

    class Meta:
        model = MarketUsers
        # 需要验证的字段
        fields = ['phone', ]

        error_messages = {
            "phone": {
                'required': "手机号码未填写"
            }
        }

    def clean_phone(self):
        # 验证手机号码是否唯一
        phone = self.cleaned_data.get('phone')
        rs = MarketUsers.objects.filter(phone=phone).exists()
        if rs:
            raise forms.ValidationError("该手机号码已被注册")
        return phone
        # 单独清洗

    def clean(self):
        # 验证密码是否一致
        password = self.cleaned_data.get("password")
        repassword = self.cleaned_data.get("repassword")

        if password and repassword and password != repassword:
            # 确认密码错误
            raise forms.ValidationError({"repassword": "两次密码输入不一致"})

        # 返回清洗后的数据
        return self.cleaned_data


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = MarketUsers
        fields = ['phone', 'password']

        error_messages = {
            'phone': {
                'required': '请填写手机号'
            },
            'password': {
                'required': '请填写密码'
            }
        }

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        try:
            user = MarketUsers.objects.get(phone=phone)
        except MarketUsers.DoesNotExist:
            raise forms.ValidationError({'phone': '手机号码错误'})

        if user.password != set_password(password):
            raise forms.ValidationError({'password': '密码错误'})
        self.cleaned_data['user'] = user
        return self.cleaned_data
