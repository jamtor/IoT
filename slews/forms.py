from cProfile import label
from django import forms
from django.contrib.auth.models import User
from slews.models import UserProfileInfo

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}),
        }
        help_texts = {
            'username' : None,
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        widgets = {
            'portfolio_site': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'customFile', 'type':'file', 'data-browse-on-zone-click': 'True'}),
        }
        labels = {
            'profile_pic': 'Profile Picture'
        }
