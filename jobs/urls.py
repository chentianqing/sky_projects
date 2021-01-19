# -*- coding: utf-8 -*-

# @Project:   jikeproject
# @Time:      2021-01-17 09:07
# @Author  :    chentianqing
# @File    :    urls.py

from django.conf.urls import url
from jobs import views

urlpatterns = [
    url(r"^joblist/",views.joblist,name="joblist"),
    url(r"^job/(?P<job_id>\d+)/$",views.detail,name="detail")
]