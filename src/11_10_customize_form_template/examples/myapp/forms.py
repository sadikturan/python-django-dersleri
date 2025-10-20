from django import forms

class ProductCreateForm(forms.Form):
    product_name = forms.CharField(label="Ürün adı", min_length=3, max_length=20, error_messages={
        "min_length": "min 3 karakter giriniz",
        "max_length": "mak 20 karakter giriniz"
    }, widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.DecimalField(label="fiyat", min_value=10, max_value=10000,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label="ürün açıklaması",widget=forms.Textarea(attrs={'class':'form-control'}))
    slug = forms.SlugField(label="url",widget=forms.TextInput(attrs={'class':'form-control'}))