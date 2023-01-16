from django.shortcuts import render, HttpResponse

# Create your views here.

def f1(request):
    return HttpResponse(f"<marquee><h1>This is my first page")


def add(request,p, q):
    r = p + q
    return HttpResponse(f"<h1> addition of {p} and {q} = {r}")

def sub(request,p, q):
    r = p - q
    return HttpResponse(f"<h1> substraction of {p} and {q} = {r}")

def multi(request,p, q):
    r = p * q
    return HttpResponse(f"<h1> multi of {p} and {q} = {r}")

def div(request,p, q):
    r = p / q
    return HttpResponse(f"<h1> divsion of {p} and {q} = {r}")

def floor(request,p, q):
    r = p // q
    return HttpResponse(f"<h1> floor division of {p} and {q} = {r}")

def modulo(request,p, q):
    r = p % q
    return HttpResponse(f"<h1> modulo of {p} and {q} = {r}")

def area_of_circle(request, r, pi = 3.14):
    area = pi ** r
    return HttpResponse(f"<h1> Area of circle is {area}")