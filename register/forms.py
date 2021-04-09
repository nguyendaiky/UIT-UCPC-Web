from django import forms
from .models import Team
import re

class teamForm(forms.ModelForm):
    team = forms.CharField(max_length = 30, label = 'Team\'s name',widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Team01' }))
    member1 = forms.CharField(max_length = 30, label = 'Name of member 1', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn A' }))
    member2 = forms.CharField(max_length = 30, label = 'Name of member 2', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn B' }))
    member3 = forms.CharField(max_length = 30, label = 'Name of member 3', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: Nguyễn Văn C' }))
    email = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: abcd@efgh.com' }))
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example: 0912345678' }))
    class Meta:
        model = Team
        fields = ['team', 'member1', 'member2', 'member3', 'email', 'phone', 'school']
        widgets = {"school":forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter your school\'s name' })}
    
    def clean_team(self, *args, **kwargs):
        team = self.cleaned_data.get("team")
        if 'Nguyen' not in team:
            raise forms.ValidationError("This is a invalid team name")
        return team 



    
        