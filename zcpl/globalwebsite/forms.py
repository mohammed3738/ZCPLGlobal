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
    quantity = forms.IntegerField(min_value=1, initial=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} ★') for i in range(1, 6)]),
        }




# class CheckoutForm(forms.Form):
#     country     = forms.CharField()
#     first_name  = forms.CharField()
#     last_name   = forms.CharField()
#     address     = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
#     city        = forms.CharField()
#     state       = forms.CharField()
#     zip_code    = forms.CharField()
#     email       = forms.EmailField()
#     phone       = forms.CharField()
#     notes       = forms.CharField(required=False,
#                                   widget=forms.Textarea(attrs={'rows':3}))

# class BankTransferForm(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     address = forms.CharField(widget=forms.Textarea)
#     phone = forms.CharField(max_length=20)
#     email = forms.EmailField()

#     transaction_id = forms.CharField(label="Bank Transaction ID", max_length=100)
#     payer_name = forms.CharField(label="Your Account Holder Name", max_length=100)
#     payer_bank_name = forms.CharField(label="Your Bank Name", max_length=100)


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


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class SignInForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)



class ContactForm(forms.Form):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        required=True
    )

class ShopContactForm(forms.ModelForm):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label="")

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


# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title', 'content','image']  # author is excluded, set in view

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