from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


def index_view(request):
    return HttpResponse('<h1>PROJECT-ORION HOME PAGE</h1>')

def about_view(request):
    return HttpResponse('<h1>PROJECT-ORION ABOUT PAGE</h1>')

def contact_view(request):
    return HttpResponse('<h1>PROJECT-ORION CONTACT PAGE</h1>')

