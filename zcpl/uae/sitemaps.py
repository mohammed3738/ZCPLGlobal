from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class UAESitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.85

    def items(self):
        return [
            "uae-home",
            "uae-contact",
        ]

    def location(self, item):
        return reverse(item)
