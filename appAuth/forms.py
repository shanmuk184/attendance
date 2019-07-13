from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.forms import forms
from django.forms import fields


class SignUpForm(UserCreationForm):
    # email = fields.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(forms.Form):
    username = fields.CharField(max_length=24)
    password = fields.CharField(max_length=24)
