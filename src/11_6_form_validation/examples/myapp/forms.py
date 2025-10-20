from django import forms

class ProductCreateForm(forms.Form):
    product_name = forms.CharField()
    price = forms.DecimalField()
    description = forms.CharField(widget=forms.Textarea)
    slug = forms.SlugField()