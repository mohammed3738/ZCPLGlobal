from django.core.management.base import BaseCommand
from globalwebsite.models import Product, SubCategory, Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Assign brand spare parts into common IT Hardware subcategories like SSD, MEMORY etc.'

    COMMON_CATEGORIES = [
        "HARD DRIVE",
        "SSD",
        "MEMORY",
        "POWER SUPPLY",
        "MOTHERBOARD",
        "STORAGE"
    ]

    BRANDS = ["DELL", "HPE", "IBM"]

    def handle(self, *args, **kwargs):
        try:
            parent_category = Category.objects.get(slug="it-hardware")
            self.stdout.write(self.style.SUCCESS(f"✅ Using existing category: {parent_category.name}"))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ 'it hardware' category with slug 'it-hardware' not found."))
            return

        for common_name in self.COMMON_CATEGORIES:
            common_slug = slugify(common_name)

            # Handle subcategory creation, catching slug uniqueness error
            common_subcat = SubCategory.objects.filter(slug=common_slug).first()
            if not common_subcat:
                common_subcat = SubCategory.objects.create(
                    name=common_name,
                    slug=common_slug,
                    category=parent_category
                )
                self.stdout.write(self.style.SUCCESS(f"✅ Created subcategory: {common_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"ℹ️ Subcategory '{common_name}' already exists."))

            total_added = 0

            for brand in self.BRANDS:
                brand_subcat_name = f"{brand} {common_name}"
                try:
                    brand_subcat = SubCategory.objects.get(name__iexact=brand_subcat_name)
                    products = Product.objects.filter(categories=brand_subcat)

                    for product in products:
                        product.categories.add(common_subcat)
                        total_added += 1

                    self.stdout.write(
                        self.style.SUCCESS(f"  ✔ {products.count()} products from '{brand_subcat_name}' assigned to '{common_name}'")
                    )
                except SubCategory.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"  ❌ SubCategory '{brand_subcat_name}' not found."))

            self.stdout.write(self.style.SUCCESS(f"✅ Total added to '{common_name}': {total_added}\n"))
