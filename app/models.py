#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Casa(models.Model):
    titulo = models.CharField(max_length=10)
    datos = JSONField()


    def __str__(self):
        return self.titulo