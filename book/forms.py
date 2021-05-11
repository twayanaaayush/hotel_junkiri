from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from index.models import Room, RoomInstance


class BookForm(forms.Form):
    check_in_date = forms.DateField (
                    required=True,
                    label="Check-in", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'check in date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')",
                        'readonly': 'True'
                        })
                    )
    check_out_date = forms.DateField (
                    required=True,
                    label="Check-out", 
                    widget=forms.DateInput(attrs={
                        'placeholder': 'check out date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')",
                        'readonly': 'True'
                        })
                    )
    room = forms.ModelChoiceField(
                    required=True,
                    label="Room",
                    queryset=Room.objects.all(),
                    widget=forms.Select(attrs={
                        'readonly': 'True'
                    })
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

class CheckInForm(forms.Form):
    def __init__(self, *args, **kwargs):

        self.kwargs = kwargs.pop('book_obj_data', None)
        self.room_id = self.kwargs.pop('room_id', None)
        self.user = self.kwargs.pop('user', None)
        self.check_in = self.kwargs.pop('check_in', None)
        self.check_out = self.kwargs.pop('check_out', None)

        super(CheckInForm, self).__init__(*args, **kwargs)

        if self.room_id and self.user:
            self.fields['user'].initial = self.user
            self.fields['check_in'].initial = self.check_in
            self.fields['check_out'].initial = self.check_out
            self.fields['room'].queryset = RoomInstance.objects.filter(room=Room.objects.filter(pk = self.room_id).first(), status__exact='U')

    user = forms.CharField(max_length=50, disabled=True)
    check_in = forms.DateField (
                    required=True,
                    widget=forms.DateInput(attrs={
                        'class': 'form-control col-md-3 mr-md-4 my-1 pl-2',
                        'placeholder': 'check in date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    check_out = forms.DateField (
                    required=True,
                    widget=forms.DateInput(attrs={
                        'class': 'form-control col-md-3 mr-md-4 my-1 pl-2',
                        'placeholder': 'check out date',
                        'onfocus': "(this.type='date')",
                        'onblur': "(this.type='text')"
                        })
                    )
    room = forms.ModelChoiceField(
                    required=True,
                    label="Room",
                    widget=forms.Select(),
                    queryset=None
                    )