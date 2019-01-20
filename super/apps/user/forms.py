from django import forms

from user import set_password
from user.models import Users


class RegisterModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'min_length': '密码不能少于6个字符',
                                   'max_length': '密码不能超过16个字符'
                               })
    re_password = forms.CharField(max_length=16,
                                  min_length=6,
                                  error_messages={
                                      'required': '重复密码不能为空',
                                      'min_length': '密码不能少于6个字符',
                                      'max_length': '密码不能超过16个字符'
                                  })

    class Meta:
        models = Users
        fields = ['user_name']
        error_messages = {

        }


class UserModelForm(forms.ModelForm):
    password = forms.CharField(max_length=16,
                               min_length=6,
                               error_messages={
                                   'required': '密码不能为空',
                                   'max_length': '密码不能大于16个字符',
                                   'min_length': '密码不能少于6个字符'
                               })

    class Meta:
        model = Users
        fields = ['user_name']
        error_message = {
            'user_name': {
                'required': '用户名不能为空',
                'max_length': '用户名不能超过20个字符',
            }
        }

    def clean(self):
        # 查询数据库验证用户名
        user_name = self.cleaned_data.get('user_name')
        try:
            user = Users.objects.get(user_name=user_name)
        except Users.DoesNotExist:
            raise forms.ValidationError({"user_name": "用户名错误"})
        # 验证密码
        password = self.cleaned_data.get('password', '')
        if user.password != set_password(password):
            raise forms.ValidationError({'password': "密码错误"})

        self.cleaned_data['user'] = user
        return self.cleaned_data
