from django import forms
from .models import CaseStudy
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CaseStudyForm(forms.ModelForm):
    detailed_description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = CaseStudy
        fields = [
            "category",
            "title",
            "short_description",
            "thumbnail",
            "detailed_description",
        ]
        widgets = {
            "short_description": forms.Textarea(attrs={"rows": 4}),
        }
