#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render


# Create your views here.
from app.models import Casa


def index(request):
    if request.POST:
        Casa.objects.create(
            titulo = request.POST['titulo'],
            datos = {'cuartos': request.POST['cuartos'],'banos':request.POST['banos'],'alberca': request.POST['alberca']}
        )
    cuartos = Casa.objects.filter(datos__cuartos = "2")
    return render(request, 'index.html', {
                                         'ard':cuartos,
    })