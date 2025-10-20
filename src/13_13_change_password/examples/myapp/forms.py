from django import forms
from django.forms import  widgets
from myapp.models import Product

# class ProductCreateForm(forms.Form):
#     product_name = forms.CharField(label="Ürün adı", min_length=3, max_length=20, error_messages={
#         "min_length": "min 3 karakter giriniz",
#         "max_length": "mak 20 karakter giriniz"
#     }, widget=forms.TextInput(attrs={'class':'form-control'}))
#     price = forms.DecimalField(label="fiyat", min_value=10, max_value=10000,widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(label="ürün açıklaması",widget=forms.Textarea(attrs={'class':'form-control'}))
#     slug = forms.SlugField(label="url",widget=forms.TextInput(attrs={'class':'form-control'}))

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','price','description','slug','image')
        error_messages = {
            "name": {
                "required": "name gerekli alan...",
                "max_length": "maksimum 50 karakter girmelisiniz."
            }
        }
        labels = {
            "name": "ürün adı",
            "price": "fiyat",
            "description": "açıklama",
            "slug": "url"
        }
        widgets = {
            "name": widgets.TextInput(attrs={"class":"form-control"}),
            "price": widgets.NumberInput(attrs={"class":"form-control"}),
            "description": widgets.TextInput(attrs={"class":"form-control"}),
            "slug": widgets.TextInput(attrs={"class":"form-control"}),
        }
        
class UploadForm(forms.Form):
    image = forms.FileField()