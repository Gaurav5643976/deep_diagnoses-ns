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


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class OrderNowForm(forms.Form):
    user_name = forms.CharField(max_length=125, required=True,
                                label='Username',)
    email_id = forms.EmailField(required=True,
                                label='Email Id',)
    age = forms.IntegerField()
    address_line_1 = forms.CharField(max_length=125, required=True,
                                     label='Address Line !',)
    city = forms.CharField(max_length=125, required=True,
                           label='City',)
    state = forms.CharField(max_length=125, required=True,
                            label='State',)
    zip_code = forms.IntegerField(required=True,
                                  label='Zip Code',)
    phone_no = forms.IntegerField(required=True,
                                  label='Phone Number', )
    suitable_date = forms.DateField(required=True,
                                    label='Suitable Date',)
    suitable_time = forms.TimeField(required=True,
                                    label='Suitable Time',)
