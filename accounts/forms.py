from django import forms
from allauth.account.forms import SignupForm


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=30, label='名前')
    company = forms.CharField(max_length=30, label='会社名', required=False)


class SignupUserForm(SignupForm):
    name = forms.CharField(max_length=30, label='名前')

    def save(self, request):
        user = super(SignupUserForm, self).save(request)
        user.name = self.cleaned_data['name']
        user.save()
        return user
