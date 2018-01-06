from django import forms

class LoginForm(forms.Form):
    """login登录表单"""
    username = forms.CharField()
    password = forms.CharField()

