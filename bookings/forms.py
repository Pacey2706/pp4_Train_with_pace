from django import forms
from .models import Client, Booking


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "phone_number",
            "address"
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["date", "time",]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
        }


class SessionForm(forms.Form):
    OPTIONS = [
        ("1", "30 minutes"), ("2", "60 minutes"),
    ]

    option = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)
