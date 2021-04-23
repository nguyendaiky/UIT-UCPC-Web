from django.shortcuts import render, redirect
from .forms import teamForm, loginForm, editForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import Team
from django.contrib.auth.decorators import login_required


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
                return redirect('register:profile')
            else:
                messages.error(request, '🙁 Team\'s name or Password is incorrect')
                return redirect('register:login')

@login_required         
def profile(request):
    data = Team.objects.filter(email=request.user.username)
    args = {'data':data, 'user':request.user}
    return render(request, 'login/profile.html', args)

class edit(View):
    def get(self, request):
        emp = Team.objects.get(email=request.user.username)
        return render(request, 'login/edit.html', {'ef':editForm, 'emp':emp})
    def post(self, request):
        if request.method == 'POST':
            ef = editForm(request.POST)
            if ef.is_valid():
                emp = Team.objects.get(email=request.user.username)
                emp.team = ef.cleaned_data.get('team')
                emp.member1 = ef.cleaned_data.get('member1')
                emp.member2 = ef.cleaned_data.get('member2')
                emp.member3 = ef.cleaned_data.get('member3')
                emp.phone = ef.cleaned_data.get('phone')
                emp.school = ef.cleaned_data.get('school')
                emp.save()
                messages.success(request, '✔️ Update success! ')
                return redirect('register:profile')
            else:
                ctx = {"ef":ef}
                messages.error(request, '❌ You entered an invalid value!')
                return render(request, 'login/edit.html', ctx)
            

def logout(request):
    auth_logout(request)
    return redirect('register:home')





