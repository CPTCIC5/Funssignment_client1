from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        fields=['about','image','phone_no','gender']
        model=Profile

