from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class UKSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.85

    def items(self):
        return [
            "uk-home",
            "uk-it-hardware",
            "uk-server",
            "uk-server-hdd-sdd",
            "uk-networking",
            "uk-server-storage",
            "uk-server-components",
            "uk-main-service",
            "uk-vmware-support",
            "uk-microsoft-support",
            "uk-contact",
        ]

    def location(self, item):
        return reverse(item)
