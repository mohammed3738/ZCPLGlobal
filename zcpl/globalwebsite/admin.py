from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms

# Register your models here.


admin.site.register(ContactMessageGlobal)
# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(SubCategory)
admin.site.register(Order)




class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    short_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)
