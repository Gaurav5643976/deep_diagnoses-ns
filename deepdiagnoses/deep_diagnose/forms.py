from django import forms


class Location(forms.Form):
    city = forms.CharField(
        required=True,
        label='City',
        max_length=32
    )
    state = forms.CharField(
        required=True,
        label='State',
        max_length=32
    )