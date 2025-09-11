from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox




# class ContactForm(forms.Form):
#     captcha = ReCaptchaField(
#         widget=ReCaptchaV2Checkbox,
#         required=True
#     )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    # phone = forms.CharField(max_length=15, required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)
