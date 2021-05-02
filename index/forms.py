from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
                    required=True,
                    label="", 
                    widget=forms.TextInput(attrs={
                        'class': 'py-4 bg-light',
                        'placeholder': 'Name'
                        })
                    )
    email = forms.CharField(
                    required=True,
                    label="", 
                    widget=forms.EmailInput(attrs={
                        'class': 'py-4 bg-light',
                        'placeholder': 'Email'
                        })
                    )
    message = forms.CharField(
                    required=True,
                    label="", 
                    widget=forms.Textarea(attrs={
                        'class': 'py-3 bg-light',
                        'placeholder': 'Message'
                        })
                    )