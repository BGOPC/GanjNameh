from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "",
        "placeholder": "Enter Your Email",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "",
        "placeholder": "Enter Your Email",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "",
        "placeholder": "Enter Your Massage",
    }))


class UploadBookletForm(forms.Form):
    pass
