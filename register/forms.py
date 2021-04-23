from django import forms
from .models import Team

class teamForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Team\'s name',widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Team01' }))
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: abcd@efgh.com' }))
    phone = forms.CharField(max_length = 12, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 0912345678' }))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'member2', 'member3', 'email', 'phone', 'school']
        widgets = {"school":forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your school\'s name' })}
    password = forms.CharField(max_length = 20, label = 'Password', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class loginForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Password', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class editForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Team\'s name',widget = forms.TextInput(attrs={'class': 'form-control'}))
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control'}))
    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control'}))
    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length = 12, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'member2', 'member3', 'phone', 'school']
        widgets = {"school":forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your school\'s name' })}
    