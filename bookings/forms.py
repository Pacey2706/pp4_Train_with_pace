from django import forms
from .models import Client, Booking, Session


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
        fields = [
            "client",
            "session",
            "date",
            "time"
        ]


class BookingDayForm(forms.Form):
    day = forms.DateField(
        widget=forms.SelectDateWidget(),
        label="Select a day",
    )


class BookingTimeForm(forms.Form):
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        widget=forms.HiddenInput()
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Select a time",
    )


class SessionForm(forms.Form):
    OPTIONS = [
        ("1", "30 minutes"), ("2", "60 minutes"),
    ]

    option = forms.ChoiceField(choices=OPTIONS, widget=forms.RadioSelect)