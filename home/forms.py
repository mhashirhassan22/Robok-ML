from django import forms
from .models import *
from allauth.account.forms import SignupForm 


class ImageForm(forms.ModelForm):    
    class Meta:
        model = ImageRequest
        fields = ["uploaded_image"]


class CustomSignupForm(SignupForm):
    company = forms.CharField(max_length=30)
    business_case = forms.CharField(max_length=1000)
    
    def save(self, request):
        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.company = str(self.cleaned_data['company'])
        user.business_case = str(self.cleaned_data['business_case'])
        user.is_active = False
        user.save()
        # You must return the original result.
        return user