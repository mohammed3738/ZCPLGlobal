from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.


admin.site.register(ContactMessageGlobal)
# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_per_page = 900
# admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(PPCQuote)
admin.site.register(PPCCategoryQuote)

class FAQInline(GenericTabularInline):
    model = FAQ
    extra = 1
    fields = ('question', 'answer', 'order')
    ordering = ('order',)

class SSDInline(admin.TabularInline):
    model = ServerSSD
    extra = 0

class HDDInline(admin.TabularInline):
    model = ServerHDD
    extra = 0

class OtherComponentInline(admin.TabularInline):
    model = ServerOtherComponent
    extra = 0

@admin.register(BuildServerRequest)
class BuildServerRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "server_brand", "created_at")
    inlines = [SSDInline, HDDInline, OtherComponentInline]


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
    inlines = [ProductImageInline, FAQInline]
    list_display = ('name', 'price', 'available', 'created')
    list_filter = ('available', 'created')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
# admin.site.register(Blog)
admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_per_page = 900


from django.utils.html import format_html

# -------------------------
# Blog Form for Admin
# -------------------------
class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  # CKEditor in admin

    class Meta:
        model = Blog
        fields = '__all__'


# -------------------------
# Tag Admin
# -------------------------
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


# -------------------------
# Category Admin
# -------------------------
@admin.register(CategoryBlog)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


# -------------------------
# Blog Admin
# -------------------------
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm  # use CKEditor in admin

    list_display = ('title', 'category', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'tags', 'author', 'created_at')
    search_fields = ('title', 'content', 'meta_title', 'meta_desc')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')

    inlines = [FAQInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_desc')
        }),
        ('Relations', {
            'fields': ('category', 'tags', 'author')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )

class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Category
        fields = '__all__'

class SubCategoryAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = SubCategory
        fields = '__all__'

class SeriesAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Series
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'slug']
    inlines = [FAQInline]

class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryAdminForm
    list_display = ['name', 'slug', 'category']
    inlines = [FAQInline]

class SeriesAdmin(admin.ModelAdmin):
    form = SeriesAdminForm
    list_display = ['name', 'slug', 'subcategory']
    list_filter = ['subcategory__category', 'subcategory']
    search_fields = ['name', 'subcategory__name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Series, SeriesAdmin)
# admin.site.register(RequestQuote)

@admin.register(RequestQuote)
class RequestQuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'product_name', 'requirements', 'submitted_at']
    search_fields = ['name', 'email', 'phone', 'product_name']
    list_filter = ['submitted_at']
    readonly_fields = ['name', 'email', 'phone', 'product_name', 'requirements', 'submitted_at']
    ordering = ("-submitted_at",)

@admin.register(VMWareRequestQuote)
class VMWareRequestQuoteAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'company_name', 'requirements', 'submitted_at']
    search_fields = ['name', 'email', 'phone', 'company_name']
    list_filter = ['submitted_at']
    readonly_fields = ['name', 'email', 'phone', 'company_name', 'requirements', 'submitted_at']
    ordering = ("-submitted_at",)

@admin.register(PPCCategory)
class PPCCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'heading']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'heading', 'sub_heading', 'is_active', 'order')
        }),
        ('Badge Bar', {
            'fields': ('badge_1', 'badge_2', 'badge_3'),
            'classes': ('collapse',)
        }),
        ('Content', {
            'fields': ('why_choose_heading', 'short_description', 'description')
        }),
        ('Images', {
            'fields': ('hero_image', 'partner_logo', 'partner_label')
        }),
        ('Testimonial', {
            'fields': ('testimonial_text',),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

class PPCProductInline(admin.TabularInline):
    model = PPCProduct
    fields = ['name', 'price', 'is_active']
    extra = 0
    show_change_link = True

@admin.register(PPCSubcategory)
class PPCSubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'is_active', 'order', 'created_at']
    list_editable = ['is_active', 'order']
    list_filter = ['category', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'category__name']
    raw_id_fields = ['category']
    inlines = [PPCProductInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('category', 'name', 'slug', 'heading', 'is_active', 'order')
        }),
        ('Content', {
            'fields': ('short_description', 'description','pointer')
        }),
        ('Images', {
            'fields': ('icon', 'hero_image')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PPCProduct)
class PPCProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "category", "subcategory", "is_active", "created_at")
    # list_filter = ['category', 'subcategory', 'is_active']
    raw_id_fields = ['category', 'subcategory']

    view_on_site = True

from django.contrib import admin
from .models import PPCService, PPCServiceImage, PPCServiceLead

class PPCServiceImageInline(admin.TabularInline):
    model = PPCServiceImage
    extra = 1

class PPCServiceCustomFieldInline(admin.TabularInline):
    model = PPCServiceCustomField
    extra = 1
    max_num = 2

@admin.register(PPCService)
class PPCServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "is_active",
        "created_at",
    )
    view_on_site = True

    search_fields = ("name",)
    list_filter = ("is_active",)

    prepopulated_fields = {
        "slug": ("name",)
    }

    inlines = [
        PPCServiceImageInline,
        PPCServiceCustomFieldInline,
    ]

class PPCServiceLeadAnswerInline(admin.TabularInline):
    model = PPCServiceLeadAnswer
    extra = 0

    fields = (
        "field_label",
        "answer",
    )

    readonly_fields = (
        "field_label",
        "answer",
    )

    can_delete = False

@admin.register(PPCServiceLead)
class PPCServiceLeadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "company_name",
        "service_name",
        "created_at",
    )

    list_filter = (
        "service",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "company_name",
        "service_name",
    )

    readonly_fields = (
        "service_name",
        "created_at",
    )

    inlines = [
        PPCServiceLeadAnswerInline,
    ]