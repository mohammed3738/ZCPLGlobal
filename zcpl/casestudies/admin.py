from django.contrib import admin
from .models import CaseStudy, CaseStudyCategory

@admin.register(CaseStudyCategory)
class CaseStudyCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)

@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
