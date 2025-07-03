from django.core.management.base import BaseCommand
from django.utils.text import slugify
from globalwebsite.models import Product, SubCategory, Category

class Command(BaseCommand):
    help = 'Migrate category to many-to-many and group products into server/spare parts groups'

    def handle(self, *args, **kwargs):
        self.stdout.write("🔄 Migrating legacy 'category' field to 'categories'...")

        # Step 1: Add current category to the new m2m field
        migrated = 0
        for product in Product.objects.all():
            if hasattr(product, 'category'):
                product.categories.add(product.category)
                migrated += 1
        self.stdout.write(f"✅ Migrated {migrated} products")

        # Step 2: Define category groupings
        category_groups = {
            "DELL SERVER": ["DELL RACK SERVER", "DELL TOWER SERVER", "DELL BLADE SERVER"],
            "HPE SERVER": ["HPE RACK SERVER", "HPE TOWER SERVER", "HPE BLADE SERVER"],
            "IBM SERVER": ["IBM RACK SERVER", "IBM TOWER SERVER", "IBM BLADE SERVER"],
            "DELL SPARE PARTS": ["DELL HARD DRIVE", "DELL SSD", "DELL MEMORY", "DELL POWER SUPPLY", "DELL MOTHERBOARD", "DELL STORAGE"],
            "HPE SPARE PARTS": ["HPE HARD DRIVE", "HPE SSD", "HPE MEMORY", "HPE POWER SUPPLY", "HPE MOTHERBOARD", "HPE STORAGE"],
            "IBM SPARE PARTS": ["IBM HARD DRIVE", "IBM SSD", "IBM MEMORY", "IBM POWER SUPPLY", "IBM MOTHERBOARD", "IBM STORAGE"]
        }

        # All parts combined for a common group
        all_spare_parts = (
            category_groups["DELL SPARE PARTS"] +
            category_groups["HPE SPARE PARTS"] +
            category_groups["IBM SPARE PARTS"]
        )

        def assign_group(parent_category_name, group_name, children_names):
            try:
                parent = Category.objects.get(name__iexact=parent_category_name)
            except Category.DoesNotExist:
                self.stderr.write(f"❌ Category '{parent_category_name}' not found.")
                return

            base_slug = slugify(group_name)
            slug = base_slug
            count = 1
            while SubCategory.objects.filter(slug=slug).exclude(category=parent).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            group_subcat, created = SubCategory.objects.get_or_create(
                name=group_name,
                slug=slug,
                category=parent
            )

            if created:
                self.stdout.write(f"✅ Created SubCategory '{group_name}' under '{parent.name}'")
            else:
                self.stdout.write(f"ℹ️ Subcategory '{group_name}' already exists.")

            total = 0
            for child in children_names:
                try:
                    subcat = SubCategory.objects.get(name__iexact=child)
                    products = Product.objects.filter(category=subcat)
                    for p in products:
                        p.categories.add(subcat)
                        p.categories.add(group_subcat)
                        total += 1
                    self.stdout.write(f"  ✔ {products.count()} products from '{child}' assigned to '{group_name}'")
                except SubCategory.DoesNotExist:
                    self.stderr.write(f"  ❌ SubCategory '{child}' not found.")
            self.stdout.write(f"✅ Total: {total} products assigned to '{group_name}'\n")

        # Step 3: Apply groups
        assign_group("DELL", "DELL SERVER", category_groups["DELL SERVER"])
        assign_group("DELL", "DELL SPARE PARTS", category_groups["DELL SPARE PARTS"])

        assign_group("HPE", "HPE SERVER", category_groups["HPE SERVER"])
        assign_group("HPE", "HPE SPARE PARTS", category_groups["HPE SPARE PARTS"])

        assign_group("IBM", "IBM SERVER", category_groups["IBM SERVER"])
        assign_group("IBM", "IBM SPARE PARTS", category_groups["IBM SPARE PARTS"])

        # Step 4: Common group for all spare parts
        common_category, _ = Category.objects.get_or_create(name="it hardware", slug="it-hardware")
        assign_group("it hardware", "SPARE PARTS", all_spare_parts)
