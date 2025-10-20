from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control form-control-user","placeholder":"Enter Email"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))
