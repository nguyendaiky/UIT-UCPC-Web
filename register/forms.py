from django import forms
from .models import Team
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

PasswordRegex = RegexValidator(r'^(?=.{6,})(?=.*[a-z]+)(?=.*\d+)(?=.*[A-Z]+)[ -~]*$')

class teamForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Team\'s name',widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos1', 'placeholder': 'example: Team01' }))
    
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'example: 0912345678'}))

    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'example: 0912345678'}))

    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'example: 0912345678'}))

    email = forms.CharField(label= 'Email', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: abcd@efgh.com' }))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'cmnd1', 'phone1', 'member2', 'cmnd2', 'phone2', 'member3', 'cmnd3', 'phone3', 'email', 'school']
        widgets = {"school":forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your school\'s name' })}
    password = forms.CharField(max_length = 20, label = 'Password', validators=[PasswordRegex], widget = forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pos5'}))

    def __init__(self, *args, **kwargs):
        super(teamForm, self).__init__(*args, **kwargs)

        # add custom error messages
        self.fields['team'].error_messages.update({
            'invalid': '⚠️ Your team\'s name is invalid!',
        })
        self.fields['member1'].error_messages.update({
            'invalid': '⚠️ Your member\'s name is invalid!',
        })
        self.fields['cmnd1'].error_messages.update({
            'invalid': '⚠️ CMND/CCCD is invalid!',
        })
        self.fields['phone1'].error_messages.update({
            'invalid': '⚠️ Phone number is invalid!',
        })
        self.fields['member2'].error_messages.update({
            'invalid': '⚠️ Your member\'s name is invalid!',
        })
        self.fields['cmnd2'].error_messages.update({
            'invalid': '⚠️ CMND/CCCD is invalid!',
        })
        self.fields['phone2'].error_messages.update({
            'invalid': '⚠️ Phone number is invalid!',
        })
        self.fields['member3'].error_messages.update({
            'invalid': '⚠️ Your member\'s name is invalid!',
        })
        self.fields['cmnd3'].error_messages.update({
            'invalid': '⚠️ CMND/CCCD is invalid!',
        })
        self.fields['phone3'].error_messages.update({
            'invalid': '⚠️ Phone number is invalid!',
        })
        self.fields['email'].error_messages.update({
            'invalid': '⚠️ Email address is invalid!',
        })
        self.fields['password'].error_messages.update({
            'invalid': '⚠️ Password must be at least 6 characters (a-z, A-Z, 0-9)!',
        })

class loginForm(forms.Form):
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length = 20, label = 'Password', widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class editForm(forms.ModelForm):
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    cmnd1 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone1 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos2', 'placeholder': 'example: 0912345678'}))

    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    cmnd2 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone2 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos3', 'placeholder': 'example: 0912345678'}))

    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    cmnd3 = forms.CharField(max_length=12, label = 'CMND/CCCD', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 381932123'}))
    phone3 = forms.CharField(max_length=11, label = 'Phone', widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'pos4', 'placeholder': 'example: 0912345678'}))
    class Meta:
        model = Team
        fields = ['member1', 'cmnd1', 'phone1', 'member2',  'cmnd2', 'phone2', 'member3', 'cmnd3', 'phone3','school']
        widgets = {"school":forms.Select(attrs={'class': 'form-control', 'id': 'pos5', 'placeholder': 'Enter your school\'s name' })}
    