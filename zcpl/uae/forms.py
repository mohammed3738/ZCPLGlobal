from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox




class ContactForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # phone = forms.CharField()
    # subject = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
