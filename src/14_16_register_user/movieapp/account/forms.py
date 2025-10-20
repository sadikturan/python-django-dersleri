from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class":"form-control form-control-user","placeholder":"Enter Email"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Password"}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not User.objects.filter(email=email).exists():
            self.add_error("email", "email ile kayıtlı bir kullanıcı yok.")

        return email

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password Again"})
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Username"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Email"})
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error("email","email daha önce kullanılmış")
        
        return email