from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'image']

class PPCCategoryQuoteForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = PPCCategoryQuote
        fields = ['name', 'email', 'phone', 'company', 'requirements']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Server Requirements'}),
        }


class PPCSubcategoryQuoteForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = PPCCategoryQuote
        fields = ['name', 'email', 'phone', 'company', 'requirements']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Server Requirements'}),
        }

        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'categories',           # if you want to include the M2M field too
            'name',
            'description',
            'short_description',
            'price',
            'image',
            'available',
            'meta_title',           # ✅ new SEO field
            'meta_description',     # ✅ new SEO field
        ]
        widgets = {
            'meta_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter custom meta title (optional)',
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter meta description (optional)',
            }),
        }


from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class PPCQuoteForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    company = forms.CharField(max_length=100)
    requirements = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)






class PPCProductForm(forms.ModelForm):
    class Meta:
        model = PPCProduct
        fields = [
            'name',
            'sub_heading',
            'price',
            'short_description',
            'pointer',
            'description',
            'hero_image',
            'is_active',
            'meta_title',
            'meta_description',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_heading': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, max_value=25)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} ★') for i in range(1, 6)]),
        }

class BankTransferForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)
    country = forms.CharField(max_length=100)

    transaction_id = forms.CharField(max_length=100)
    payer_name = forms.CharField(max_length=100)
    payer_bank_name = forms.CharField(max_length=100)

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Name',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Email Address',
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        })
    )

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={
            'placeholder': 'Username or Email',
            'class': 'form-control',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        })
    )

class ContactForm(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        required=True
    )

class ShopContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        required=True
    )
    class Meta:
        model = ContactMessageGlobal
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number (optional)', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 4}),
        }

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'tags', 'image', 'meta_title', 'meta_desc']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'phone', 'subject', 'message']

class CategoryForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    meta_title = forms.CharField(max_length=150, required=False)
    meta_description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'meta_title', 'meta_description']

class SubCategoryForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    meta_title = forms.CharField(max_length=150, required=False)
    meta_description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = SubCategory
        fields = ['category', 'name', 'slug', 'description', 'meta_title', 'meta_description']
               
class ContactMessageGlobalForm(forms.ModelForm):
    class Meta:
        model = ContactMessageGlobal
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number',
                'required': True
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us what you need',
                'required': True
            }),
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address",
                "required": True,
            })
        }


# *************Vaishnavi
from django import forms
# from captcha.fields import CaptchaField

from .models import PPCServiceLead


class PPCServiceLeadForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        required=True
    )
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = PPCServiceLead

        fields = [
            "name",
            "email",
            "phone",
            "company_name",
            "requirements",
            
        ]
        

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Name *",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "Email *",
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Phone *",
                "maxlength": "10",
                "minlength": "10",
                "inputmode": "numeric",
                "oninput": "this.value = this.value.replace(/[^0-9]/g, '').slice(0, 10);",
            }),

            "company_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Company Name",
            }),

            "requirements": forms.Textarea(attrs={
                "class": "form-input",
                "placeholder": "Specify Your Requirements *",
                "rows": 3,
            }),
        }
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only numbers."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return phone

    def __init__(self, *args, service=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.service = service

        if service:
            for custom_field in service.custom_fields.all():

                field_name = f"custom_{custom_field.id}"

                if custom_field.field_type == "dropdown":

                    options = [
                        (option.strip(), option.strip())
                        for option in custom_field.dropdown_options.split(",")
                        if option.strip()
                    ]

                    options.insert(0, ("", f"Select {custom_field.label}"))

                    self.fields[field_name] = forms.ChoiceField(
                        label=custom_field.label,
                        choices=options,
                        required=custom_field.is_required,
                        widget=forms.Select(attrs={
                            "class": "form-input"
                        })
                    )

                else:

                    self.fields[field_name] = forms.CharField(
                        label=custom_field.label,
                        required=custom_field.is_required,
                        widget=forms.TextInput(attrs={
                            "class": "form-input",
                            "placeholder": custom_field.label
                        })
                    )