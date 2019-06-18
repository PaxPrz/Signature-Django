from django import forms
from sign.models import Custom_user


class Custom_user_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Custom_user
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'photo')
