from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from .models import User
from index.models import Room


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
            'u_contact': forms.NumberInput(attrs={'placeholder': 'Contact Number'}),
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


class BookForm(forms.Form):
    check_in_date = forms.DateField (
                    required=True,
                    label="Check-in", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'check in date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    check_out_date = forms.DateField (
                    required=True,
                    label="Check-out", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'check out date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    room = forms.ModelChoiceField(
                    required=True,
                    label="Room",
                    queryset=Room.objects.all(),
                    widget=forms.Select()
                    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class="col-sm-3 text-muted"
        self.helper.field_class="col-sm-9"
        self.helper.form_class = "form-horizontal"
        self.helper.layout = Layout(
            'check_in_date',
            'check_out_date',
            'room'
        )