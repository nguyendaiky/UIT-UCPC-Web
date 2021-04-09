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
    tf = teamForm(request.POST or None)
    if tf.is_valid():
        tf.save()
        tf = teamForm()
    context = {'tf': teamForm}
    return render(request, 'register/register.html', context)




