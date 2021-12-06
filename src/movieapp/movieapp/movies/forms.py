from django import forms
from django.forms import widgets
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        numbers = (
            ('1','1 Yıldız'),
            ('2','2 Yıldız'),
            ('3','3 Yıldız'),
            ('4','4 Yıldız'),
            ('5','5 Yıldız'),
        )
        model = Comment
        # fields = ['full_name','email','text','rating']
        exclude = ['movie','date_added',]
        labels = {
            "full_name":"Ad Soyad",
            "email": "Eposta",
            "text": "Yorum",
            "rating": "Puan"
        }
        widgets = {
            "full_name": widgets.TextInput(attrs={"class":"form-control"}),
            "email": widgets.EmailInput(attrs={"class":"form-control"}),
            "text": widgets.Textarea(attrs={"class":"form-control"}),
            "rating": widgets.Select(attrs={"class":"form-control custom-select"}, choices= numbers),
        }