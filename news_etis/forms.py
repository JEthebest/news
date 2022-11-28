from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ('login', 'password')
        
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        if len(password) <= 8:
            raise forms.ValidationError(
                "password too short"
            )
