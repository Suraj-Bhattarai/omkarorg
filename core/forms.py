from django import forms
from core.models import Product ,Service
from django.forms import ModelForm,DateTimeInput,DateTimeField, TextInput, Textarea, Select, FileInput, NumberInput ,NullBooleanSelect


class ProductForms(ModelForm):
    class Meta():
        model = Product
        fields = ('price', 'title', 'features','specification','description',
                  'category', 'subcategory',
                  'brand', 'color','model_no','best_seller',
                  'product_brocher','easymart_link',
                  'warrenty_type', 'warrenty_period',
                  'cloudName','photo_tag','video_tag','image_url','product_type'
                  )
        widgets = {
            'price': NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Rs. 00000'}),
            'title': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Samsung A50'}),

            'category': Select(
                attrs={'class': 'select2 form-control'}),
            'subcategory': Select(
                attrs={'class': 'select2 form-control'}), 
            
            'features': Textarea(
                attrs={'class': 'form-control'}),
            'description': Textarea(
                attrs={'class': 'form-control'}),
            'specification': Textarea(
                attrs={'class': 'form-control'}),

            'brand': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Samsung'}),
            'color': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Red'}),
            'model_no': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'A50'}),
            'best_seller': NullBooleanSelect(
                attrs={'class': 'form-control'}),

            'product_brocher': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Add File to Google Drive and put the link here.'}),
            'easymart_link': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'www.easymartnepal.com/'}),

            'warrenty_type': TextInput(
                attrs={'class': 'form-control', 'placeholder': ' Hardware Warrenty'}),
            'warrenty_period': TextInput(
                attrs={'class': 'form-control', 'placeholder': ' 1 Year'}),   

            'cloudName': TextInput(
                attrs={'class': 'form-control'}),
            'photo_tag': TextInput(
                attrs={'class': 'form-control'}),  
            'video_tag': TextInput(
                attrs={'class': 'form-control'}),  
            'image_url': TextInput(
                attrs={'class': 'form-control'}),

            'product_type': Select(
                attrs={'class': 'select2 form-control'}),      
        }



class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })



class ServiceForm(ModelForm):

    # estimate_time = DateTimeField()

    class Meta():
        model = Service
        fields = ('price', 'customer_name', 'tracking_code','estimate_time',
                  'status', 'note','product_name')
        widgets = {
            'price': NumberInput(
                attrs={'class': 'form-control'}),
            'customer_name': TextInput(
                attrs={'class': 'form-control'}),
            'status': Select(
                attrs={'class': 'select2 form-control'}),
            'tracking_code': TextInput(
                attrs={'class': 'form-control'}),
            'note': Textarea(
                attrs={'class': 'form-control', 'rows':'2'}),
            'product_name': TextInput(
                attrs={'class': 'form-control'}),   

            'estimate_time': DateTimeInput(format='%Y-%m-%d %H:%M:%S',attrs={'class': 'datetimefield form-control' ,'type':'datetime','placeholder': 'Pick a date'})
             
            # 'estimate_time': DateTimeInput( attrs={'class': 'form-control','type':'datetime-local'}),

        }


