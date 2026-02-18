from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.


admin.site.register(ContactMessageGlobal)
# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Review)
# admin.site.register(SubCategory)
admin.site.register(Order)
admin.site.register(PPCQuote)


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
    inlines = [ProductImageInline]
    list_display = ('name', 'price', 'available', 'created')
    list_filter = ('available', 'created')
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)
# admin.site.register(Blog)
admin.site.register(Comment)



from django.utils.html import format_html

# ------------------------
# Category Admin
# ------------------------
# class SubCategoryBlogInline(admin.TabularInline):
#     model = SubCategoryBlog
#     extra = 1
#     fields = ('name', 'slug')
#     readonly_fields = ('slug',)

# @admin.register(CategoryBlog)
# class CategoryBlogAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug', 'subcategories_count')
#     search_fields = ('name',)
#     # inlines = [SubCategoryBlogInline]
#     prepopulated_fields = {"slug": ("name",)}

#     def subcategories_count(self, obj):
#         return obj.subcategories.count()
#     subcategories_count.short_description = "SubCategories"


# # ------------------------
# # SubCategory Admin
# # ------------------------
# @admin.register(SubCategoryBlog)
# class SubCategoryBlogAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'slug')
#     list_filter = ('category',)
#     search_fields = ('name', 'category__name')
#     prepopulated_fields = {"slug": ("name",)}


# ------------------------
# Tag Admin
# ------------------------



# ------------------------
# Blog Admin
# ------------------------
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'subcategory', 'author', 'created_at', 'updated_at', 'tag_list')
#     list_filter = ('category', 'tags', 'author', 'created_at')
#     search_fields = ('title', 'content', 'category__name', 'tags__name', 'author__username')
#     prepopulated_fields = {"slug": ("title",)}
#     date_hierarchy = 'created_at'  # This provides the archive by year/month

#     def tag_list(self, obj):
#         return ", ".join([tag.name for tag in obj.tags.all()])
#     tag_list.short_description = "Tags"



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


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ['name', 'slug']


class SubCategoryAdmin(admin.ModelAdmin):
    form = SubCategoryAdminForm
    list_display = ['name', 'slug', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)


@admin.register(PPCProduct)
class PPCProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "is_active", "created_at")
    view_on_site = True
