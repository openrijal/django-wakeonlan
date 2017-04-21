# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Name of Machine")
    mac_addr = models.CharField(max_length=20, verbose_name="MAC Address")
