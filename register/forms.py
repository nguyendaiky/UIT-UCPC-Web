from django import forms
from .models import Team
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class teamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team', 'member1', 'member2', 'member3', 'email', 'phone', 'school']

        widgets = {
            'team': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Team01' }),
            'member1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }),
            'member2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }),
            'member3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: abcd@efgh.com' }),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 0912345678' }),
            'school': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your school\'s name' }),
        }

    
        