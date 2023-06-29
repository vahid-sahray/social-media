from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password' ,widget=forms.PasswordInput)   


    def clean_email(self):
        email = self.cleaned_data['email']
        user =  User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        user =  User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already exists')
        return username


    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('password must much')
        

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='password' ,widget=forms.PasswordInput)
