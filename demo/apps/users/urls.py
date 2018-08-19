# -*- coding: utf-8 -*-
# @Time    : 18-8-19 下午4:37
# @Author  : kimi_ming
# @File    : urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/(?P<username>[a-z]{5,20})/$', views.RegisterUserNameView.as_view())
]
