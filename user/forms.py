from django import forms
from django.forms.widgets import TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .models import User

class PhoneInput(TextInput):
    input_type = 'tel'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['u_room']
        labels = {
            'u_name': 'Name',
            'u_email': 'Email',
            'u_contact': 'Contact',
            'u_address': 'Address',
        }
        widgets = {
            'u_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'u_email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'u_contact': PhoneInput(attrs={'placeholder': 'Contact Number'}),
            'u_address': forms.TextInput(attrs={'placeholder': 'Address'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class="col-sm-3 small text-muted"
        self.helper.field_class="col-sm-9"
        self.helper.form_class = "form-horizontal"
        self.helper.layout = Layout(
            'u_name',
            'u_email',
            'u_contact',
            'u_address'
        )

