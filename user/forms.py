from django import forms
from .models import User
from index.models import Room


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['u_room']
        labels = {
            'u_name': '',
            'u_email': '',
            'u_contact': '',
            'u_address': '',
        }
        widgets = {
            'u_name': forms.TextInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'Name',
                        }),
            'u_email': forms.EmailInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'Email',
                        }),
            'u_contact': forms.NumberInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'Contact Number',
                        }),
            'u_address': forms.TextInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'Address',
                        }),
        }


class BookForm(forms.Form):
    check_in_date = forms.DateField (
                    required=True,
                    label="", 
                    widget=forms.DateInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'check in date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    check_out_date = forms.DateField (
                    required=True,
                    label="", 
                    widget=forms.DateInput(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        'placeholder': 'check out date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    room = forms.ModelChoiceField(
                    required=True,
                    label="",
                    queryset=Room.objects.all(),
                    widget=forms.Select(attrs={
                        'class': 'form-control mr-md-4 my-1 pl-2',
                        })
                    )