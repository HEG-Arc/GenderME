# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Surname(models.Model):
    surname = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=6)
    language = models.CharField(max_length=2)
