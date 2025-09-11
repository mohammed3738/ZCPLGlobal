from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100,
#         required=True,
#         label="Your Name",
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter your name',
#             'class': 'form-control'
#         })
#     )

#     email = forms.EmailField(
#         required=True,
#         label="Email Address",
#         widget=forms.EmailInput(attrs={
#             'placeholder': 'Enter your email',
#             'class': 'form-control'
#         })
#     )

#     phone = forms.CharField(
#         max_length=15,
#         required=True,
#         label="Phone Number",
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Enter your phone number',
#             'class': 'form-control'
#         })
#     )

#     subject = forms.CharField(
#         max_length=200,
#         required=True,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Subject',
#             'class': 'form-control'
#         })
#     )

#     message = forms.CharField(
#         required=True,
#         label="Write Message",
#         widget=forms.Textarea(attrs={
#             'placeholder': 'Type your message here...',
#             'class': 'form-control',
#             'rows': 5
#         })
#     )
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())



class ContactForm(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        required=True
    )


# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(max_length=15, required=True)
#     subject = forms.CharField(max_length=200, required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)
#     captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, required=True)
