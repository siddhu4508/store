from re import I
from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return HttpResponse("hello world!")