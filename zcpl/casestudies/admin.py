from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import CaseStudy, FAQ


class FAQInline(GenericTabularInline):
    model = FAQ
    extra = 1
    fields = ('question', 'answer', 'order')


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "created_at")
    inlines = [FAQInline]