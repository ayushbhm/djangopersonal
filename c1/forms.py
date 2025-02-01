# c1/forms.py
from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email']

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)  # or super().save(commit=False) in Python 3
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
