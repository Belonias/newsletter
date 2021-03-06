from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

    # email validator
    # we can use the clean_email function
    # from SignUpForm class


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        # email validator
        '''
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not domain == 'USC':
            raise forms.ValidationError("Plase use USC email")
        if not extension == "edu":
            raise forms.ValidationError("Please use valid college email adress")
            '''
        return email


    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name
