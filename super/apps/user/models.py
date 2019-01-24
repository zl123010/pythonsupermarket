from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.


class MarketUsers(models.Model):
    sex_choices = {
        (1, "男"),
        (2, "女"),
    }
    phone = models.CharField(max_length=11,
                             verbose_name="手机号码",
                             validators=[
                                 RegexValidator(r'^1[3-9]\d{9}$', "手机号码格式错误!")
                             ])
    nick_name = models.CharField(max_length=50,
                                 null=True,
                                 blank=True,
                                 verbose_name="昵称"
                                 )
    password = models.CharField(max_length=32,
                                verbose_name="密码"
                                )
    gender = models.SmallIntegerField(choices=sex_choices,
                                      default=2,
                                      verbose_name="性别")
    birthday = models.DateField(null=True,
                                blank=True,
                                verbose_name="生日"
                                )
    school = models.CharField(max_length=50,
                              null=True,
                              blank=True,
                              verbose_name="学校")
    hometown = models.CharField(max_length=50,
                                null=True,
                                blank=True,
                                verbose_name="家庭地址")
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               verbose_name="住址")
    head = models.ImageField(upload_to="head/%Y%m", default='head/memtx.png')

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'mk_users'
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name
