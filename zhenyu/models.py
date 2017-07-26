# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    pass
class Usa(models.Model):
    number=models.CharField(max_length=32)
    name=models.CharField(max_length=32)