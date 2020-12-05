from django.shortcuts import render


def landing_page(req):
    return render(req, 'landing_page.html')


def original(req):
    return render(req, 'landing_page.html')
# Create your views here.
