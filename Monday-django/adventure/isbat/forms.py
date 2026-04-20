from django import forms
from isbat.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','Last_name','password1','password2','email']