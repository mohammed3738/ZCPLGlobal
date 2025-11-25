from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import *

def case_study_list(request):
    case_studies = CaseStudy.objects.all().order_by('-created_at')
    categories = CaseStudyCategory.objects.all()

    return render(request, "casestudies/list.html", {
        "case_studies": case_studies,
        "case_study_categories": categories,
    })


def case_study_detail(request, slug):
    case_study = get_object_or_404(CaseStudy, slug=slug)

    related = CaseStudy.objects.filter(
        category=case_study.category
    ).exclude(id=case_study.id).order_by('-created_at')[:3]

    return render(request, "casestudies/detail.html", {
        "case_study": case_study,
        "related_case_studies": related,
        "case_study_categories": CaseStudyCategory.objects.all(),
    })



def case_studies_by_category(request, slug):
    category = get_object_or_404(CaseStudyCategory, slug=slug)
    case_studies = CaseStudy.objects.filter(category=category)
    categories = CaseStudyCategory.objects.all()

    return render(request, "casestudies/list.html", {
        "case_studies": case_studies,
        "case_study_categories": categories,
        "selected_category": category,
    })
