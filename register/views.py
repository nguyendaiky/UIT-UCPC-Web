from django.shortcuts import render, redirect
from .forms import teamForm, loginForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.
def home(request):
    context = {}
    return render(request, 'register/home.html', context)

class register(View):
    def get(self, request):
        context = {'tf': teamForm}
        return render(request, 'register/register.html', context)
    
    def post(self, request):
        if request.method == 'POST':
            tf = teamForm(request.POST)
            if tf.is_valid():
                Username = request.POST['team']
                Email = request.POST['email']
                Password = request.POST['password']
                tf.save()
                user = User.objects.create_user(Email, Email, Password)
                Team = tf.cleaned_data.get('team')
                messages.success(request, '✔️ Account was created for '+Team)
                return redirect('register:login')
            else:
                ctx = {"tf":tf}
                messages.error(request, '❌ You entered an invalid value!')
                return render(request, 'register/register.html', ctx)
                

class login(View):
    def get(self, request):
        ctx = {'lf': loginForm}
        return render(request, 'login/login.html', ctx)
    def post(self, request):
        if request.method == 'POST':
            Username = request.POST['email']
            Password = request.POST['password']

            user = authenticate(request, username=Username, password=Password)

            if user is not None:
                auth_login(request, user)
                return redirect('register:home')
            else:
                messages.error(request, '🙁 Team\'s name or Password is incorrect')
                return redirect('register:login')
                






