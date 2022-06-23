from django.db import models
from django import forms
# Create your models here.
from django.forms import widgets
from django.core.validators import RegexValidator  # 正则验证
from django.forms import widgets as wds  # 自定义表单属性的插件


class UserInfo(models.Model):
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class UserForm(forms.Form):
    username = forms.CharField(min_length=4, label='用户名',
                               widget=widgets.TextInput(attrs={"class": "form-control"}),
                               error_messages={
                                   "required": "用户名不能为空",
                               })
    pwd = forms.CharField(min_length=4, label='密码',
                          error_messages={
                              "required": "密码不能为空",
                          },
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    r_pwd = forms.CharField(min_length=4, label='确认密码',
                            widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                            error_messages={
                                "required": "密码不能为空"})
