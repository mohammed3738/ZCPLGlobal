import os
from django.core.management.base import BaseCommand
from django.conf import settings
from globalwebsite.models import Product, ProductImage, Blog
from PIL import Image

class Command(BaseCommand):
    help = 'Convert existing images to WebP and resize'

    def process_image(self, image_path, size):
        if not os.path.exists(image_path):
            return None
        img = Image.open(image_path)
        img = img.convert('RGB')
        # Updated for Pillow >=10
        img.thumbnail(size, Image.Resampling.LANCZOS)
        webp_path = os.path.splitext(image_path)[0] + '.webp'
        img.save(webp_path, 'WEBP', quality=80)
        return webp_path

    def handle(self, *args, **kwargs):
        # Product main images
        for product in Product.objects.all():
            if product.image:
                path = os.path.join(settings.MEDIA_ROOT, product.image.name)
                new_path = self.process_image(path, (800, 800))
                if new_path:
                    product.image.name = os.path.relpath(new_path, settings.MEDIA_ROOT)
                    product.save()
                    self.stdout.write(f"Converted Product: {product.name}")

        # Product gallery images
        for img in ProductImage.objects.all():
            if img.image:
                path = os.path.join(settings.MEDIA_ROOT, img.image.name)
                new_path = self.process_image(path, (800, 800))
                if new_path:
                    img.image.name = os.path.relpath(new_path, settings.MEDIA_ROOT)
                    img.save()
                    self.stdout.write(f"Converted Gallery Image: {img.product.name}")

        # Blog images
        for blog in Blog.objects.all():
            if blog.image:
                path = os.path.join(settings.MEDIA_ROOT, blog.image.name)
                new_path = self.process_image(path, (1200, 800))
                if new_path:
                    blog.image.name = os.path.relpath(new_path, settings.MEDIA_ROOT)
                    blog.save()
                    self.stdout.write(f"Converted Blog: {blog.title}")
