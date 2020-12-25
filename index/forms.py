from django import forms

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