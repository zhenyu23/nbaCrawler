# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

from zhenyu import models

# Create your views here.
from zhenyu.process import test

def hello(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password",None)
        print (username,password)
        return render_to_response("hello.html")


def default(request):
    # new_name = ''
    zhenyu_info = models.Info().objects.filter()
    #
    # if not zhenyu_info:
    #     pass
    zhenyu_info.name='a'
    zhenyu_info.sex='a'
    zhenyu_info.info='a'
    zhenyu_info.save()

    zhenyu_list = models.Info.objects.filter()

    print test.test_process()

    # name = 'zhenyu'
    # sex = '?'
    # age='17'
    return render_to_response('default.html',locals())

def zhenyu(request):
    return render_to_response('zhenyu.html')
