from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import CaseStudy


class CaseStudyListSitemap(Sitemap):
    priority = 0.80
    changefreq = "weekly"

    def items(self):
        return ["case_study_list"]

    def location(self, item):
        return reverse(item)


class CaseStudyDetailSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.75

    def items(self):
        return CaseStudy.objects.all()

