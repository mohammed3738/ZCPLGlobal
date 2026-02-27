from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Category, SubCategory
from .models import Product




class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.85

    def items(self):
        return Category.objects.order_by("slug")

    def location(self, obj):
        return f"/shop/{obj.slug}/"


class SubCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.80

    def items(self):
        return SubCategory.objects.select_related("category").order_by(
            "category__slug", "slug"
        )

    def location(self, obj):
        return f"/shop/{obj.category.slug}/{obj.slug}/"



class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.85

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return None  # if you have updated_at field

    def location(self, obj):
        return f"/product/{obj.slug}/"  # OR obj.get_absolute_url()


class StaticViewSitemap(Sitemap):

    def items(self):
        return [
            {"url": "home", "priority": 1.0, "changefreq": "daily"},
            {"url": "services", "priority": 0.85, "changefreq": "weekly"},
            {"url": "about_us", "priority": 0.75, "changefreq": "monthly"},
            {"url": "contact", "priority": 0.85, "changefreq": "monthly"},
            {"url": "it-hardware", "priority": 0.85, "changefreq": "weekly"},
            {"url": "server-maintenance", "priority": 0.85, "changefreq": "weekly"},
            {"url": "storage-maintenance", "priority": 0.85, "changefreq": "weekly"},
            {"url": "network-maintenance", "priority": 0.85, "changefreq": "weekly"},
            {"url": "vmware-support", "priority": 0.85, "changefreq": "weekly"},
            {"url": "microsoft-thirdparty-support", "priority": 0.85, "changefreq": "weekly"},
            {"url": "build-your-server", "priority": 0.85, "changefreq": "weekly"},
            {"url": "rental-services", "priority": 0.85, "changefreq": "weekly"},
            {"url": "global-it", "priority": 0.85, "changefreq": "weekly"},
            {"url": "privacy", "priority": 0.64, "changefreq": "yearly"},
            {"url": "term", "priority": 0.64, "changefreq": "yearly"},
        ]

    def location(self, item):
        return reverse(item["url"])

    def priority(self, item):
        return item["priority"]

    def changefreq(self, item):
        return item["changefreq"]


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.75

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        try:
            return obj.get_absolute_url()
        except Exception:
            return f"/blogs/{obj.slug}/"


