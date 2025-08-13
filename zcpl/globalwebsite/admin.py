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


class ProductImageInline(admin.TabularInline):  # You can use StackedInline if you want bigger fields
    model = ProductImage
    extra = 1  # Number of empty image upload fields
    fields = ('image',)
    readonly_fields = ()
    classes = ['collapse']  # Makes it collapsible


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductImageInline]
    list_display = ('name', 'price', 'available', 'created')
    list_filter = ('available', 'created')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)



