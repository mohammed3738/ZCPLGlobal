from django.contrib import admin
from .models import CaseStudy

# class CaseStudyCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}
#     list_display = ("name",)

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "created_at")
