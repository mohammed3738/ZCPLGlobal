



from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class IndiaStaticSitemap(Sitemap):
    priority = 0.85
    changefreq = "weekly"

    def items(self):
        return [
            "india-home",
            "india-contact",
            "india-services",
            "it-hardware-india",
            "server-maintenance-india",
            "storage-maintenance-india",
            "network-maintenance-india",
            "rental-services-india",
            "infrastructure-managed-service-india",
            "refurbished-servers-mumbai",
            "refurbished-servers-bangalore",
            "refurbished-servers-chennai",
            "refurbished-servers-kolkata",
            "refurbished-servers-ahmedabad",
            "refurbished-servers-hyderabad",
            "refurbished-servers-pune",
            "refurbished-servers-delhi",
        ]

    def location(self, item):
        return reverse(item)
