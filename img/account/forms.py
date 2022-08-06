from  django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    passwword = forms.CharField(widget=forms.PasswordInput)