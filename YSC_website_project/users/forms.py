from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.db import models

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-element-label"})
        self.fields["email"].widget.attrs.update({"class": "form-element-label"})
        self.fields["password1"].widget.attrs.update({"class": "form-element-label"})
        self.fields["password2"].widget.attrs.update({"class": "form-element-label"})
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'alias', 'location']