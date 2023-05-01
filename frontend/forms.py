from django import forms
from .models import Booklet


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "",
        "placeholder": "Enter Your Name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "",
        "placeholder": "Enter Your Email",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "",
        "placeholder": "Enter Your Massage",
    }))


class UploadBookletForm(forms.ModelForm):
    class Meta:
        model = Booklet
        fields = ('name', 'description', 'category', 'booklet_file')
        widgets = {
            'category': forms.Select(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': 'Category'
            }),
            'name': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': 'Name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': 'Description'
            }),
            'booklet_file': forms.ClearableFileInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white',
                'placeholder': 'Booklet File'
            }),
        }
