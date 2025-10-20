from django import forms

class ProductCreateForm(forms.Form):
    product_name = forms.CharField(label="Ürün adı",required=False, min_length=3, max_length=20, error_messages={
        "min_length": "min 3 karakter giriniz",
        "max_length": "mak 20 karakter giriniz"
    })
    price = forms.DecimalField(label="fiyat", min_value=10, max_value=10000)
    description = forms.CharField(label="ürün açıklaması",widget=forms.Textarea)
    slug = forms.SlugField(label="url")