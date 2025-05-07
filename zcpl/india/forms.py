from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        })
    )

    phone = forms.CharField(
        max_length=15,
        required=True,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your phone number',
            'class': 'form-control'
        })
    )

    subject = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control'
        })
    )

    message = forms.CharField(
        required=True,
        label="Write Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your message here...',
            'class': 'form-control',
            'rows': 5
        })
    )
