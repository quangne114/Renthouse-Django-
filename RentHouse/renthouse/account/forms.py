from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth', 'email', 'username','Url_account', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Enter Your Birthday'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['Url_account'].widget.attrs['placcholer'] = 'Enter Url'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-group'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'Url_account']