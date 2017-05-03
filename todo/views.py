# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from todo.models import Casino, Todo
from todo.serializers import CasinoSerializer, TodoSerializer


class ListCreateCasinos(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer


class ListCreateTodos(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
