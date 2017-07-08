from django.contrib.auth.forms import AuthenticationForm
from django import forms


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    type_1 = 'Admin'
    type_2 = 'Volunteer'
    TYPE_CHOICES = (
        (type_1, u"Admin"),
        (type_2, u"Volunteer"))
    type = forms.ChoiceField(label="type", choices=TYPE_CHOICES)

    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


