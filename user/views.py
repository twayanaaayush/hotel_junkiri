from django.http.response import HttpResponse
from django.shortcuts import render


def book(request):
    return HttpResponse('<h1>BOOKING PAGE</h1>')