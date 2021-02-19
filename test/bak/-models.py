# -*-coding:utf-8 -*-
"""
-------------------------------------------------------------------------------
@author  :sdc_os
@time    :2020/02/10
@file    :api_url.py
@desc    :基本的models
@license :(c) Copyright 2020, SDC.
-------------------------------------------------------------------------------
"""
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AuthToken(Token):
    """
    name:用户访问Token表
    """
    started = models.DateTimeField(_("Started"), auto_now_add=True)
    expires = models.DateTimeField(_("Expires"), null=True)


class ProfileUserMetaclass(type):
    """
    用户元类
    """
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        fields = []
        for obj_name, obj in attrs.items():
            if isinstance(obj, models.Field):
                fields.append(obj_name)
            User.add_to_class(obj_name, obj)
        UserAdmin.fieldsets = list(UserAdmin.fieldsets)
        UserAdmin.fieldsets.append((name, {'fields': fields}))
        return type.__new__(cls, name, bases, attrs)


class ProfileUser(object, metaclass=ProfileUserMetaclass):
    GENDER = (
        ('M', "男"),
        ('W', "女"),
    )
    USER_CATEGORY = (
        ('0', '自然人'),
        ('1', '系统'),
    )
    department = models.CharField(_("Department"), max_length=255, blank=True, null=True)
    synced = models.DateTimeField(_("Synced"), null=True)
    avatar = models.TextField(_("Avatar"), blank=True, null=True)
    short_name = models.CharField(_("ShortName"), max_length=16, blank=True, null=True)
    sex = models.CharField(_("Sex"), max_length=2, choices=GENDER, blank=True, null=True)
    category = models.CharField(
        _("Category"), max_length=4, choices=USER_CATEGORY, default='0', blank=True, null=True)

    def display_department(self, start_index=1, end_index=3):
        if self.department is None:
            return ""
        else:
            return "\\".join(self.department.split('\\')[start_index:end_index])


class Base(models.Model):
    """
    基础表，后续的app中models的定义都继承此表
    """
    creator = models.CharField(verbose_name="创建人用户名", max_length=50, blank=False, null=False, )
    last_mender = models.CharField(verbose_name="最后修改人用户名", max_length=50, blank=False, null=False)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    last_modified_time = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)

    class Meta:
        abstract = True
