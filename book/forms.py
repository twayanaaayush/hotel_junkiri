from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from index.models import Room


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


class AvailabilityForm(forms.Form):
    check_in = forms.DateField (
                    # default=date.today,
                    required=True,
                    label="", 
                    widget=forms.DateInput(attrs={
                        'class': 'form-control col-md-3 mr-md-4 my-1 pl-2',
                        'placeholder': 'check in date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    check_out = forms.DateField (
                    required=True,
                    label="", 
                    widget=forms.DateInput(attrs={
                        'class': 'form-control col-md-3 mr-md-4 my-1 pl-2',
                        'placeholder': 'check out date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    num_guests = forms.IntegerField (
                    required=True,
                    label="",
                    widget=forms.NumberInput(attrs={
                        'class': 'form-control col-md-2 mr-md-4 my-1 pl-2',
                        'placeholder': 'guests'
                        })
                    )