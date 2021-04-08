from django.shortcuts import render, redirect
from .forms import teamForm
from django.http import HttpResponse
import re
from .models import TeamRegex, NameRegex, PhoneRegex

# Create your views here.
def home(request):
    context = {}
    return render(request, 'register/home.html', context)

def register(request):
    context = {'tf': teamForm}
    return render(request, 'register/register.html', context)

def getForm(request):
    if request.method == "POST":
        tf = teamForm(request.POST)
        if tf.is_valid():
            tf.save()
            ctx = {"st": "Success! Thanks for register UCPC!", "tf": tf}
            return render(request, 'register/success.html', ctx)
        else:
            ctx = {"st": "Invalid value! Try again!"}
            return render(request, 'register/fail.html', ctx)




