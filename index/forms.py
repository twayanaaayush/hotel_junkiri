from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
                    required=True,
                    label="Name", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'Name'
                        })
                    )
    email = forms.CharField(
                    required=True,
                    label="Email", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'Email'
                        })
                    )
    message = forms.CharField(
                    required=True,
                    label="Message", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'Message'
                        })
                    )