from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class UKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.85

    def items(self):
        return [
            "uk-home",
            "uk-contact",
        ]

    def location(self, item):
        return reverse(item)
