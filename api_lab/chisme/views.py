# -*- coding: utf-8 -*-
from django.shortcuts import render

from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class ChismeModelViewSet(viewsets.ModelViewSet):
    queryset = models.Chisme.objects.all()
    serializer_class = serializers.ChismeSerializer