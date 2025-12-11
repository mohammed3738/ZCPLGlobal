from django.contrib.sitemaps import Sitemap
from .models import Product  # your product model

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return None  # if you have updated_at field

    def location(self, obj):
        return f"/product/{obj.slug}/"  # OR obj.get_absolute_url()
