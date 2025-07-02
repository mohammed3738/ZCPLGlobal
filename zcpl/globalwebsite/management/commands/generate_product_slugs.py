from django.core.management.base import BaseCommand
from django.utils.text import slugify
from globalwebsite.models import Product

class Command(BaseCommand):
    help = 'Generate slugs for existing products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        updated = 0

        for product in products:
            if not product.slug:
                base_slug = slugify(product.name)
                slug = base_slug
                counter = 1
                while Product.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                product.slug = slug
                product.save()
                updated += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated} products with slugs."))
