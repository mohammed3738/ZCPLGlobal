from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, Transpose
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import strip_tags

# Create your models here.

# from django import forms

class ContactMessageGlobal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject} - {self.submitted_at}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True, null=True)

    # ✅ SEO fields
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Auto-generate slug if missing
        if not self.slug:
            self.slug = slugify(self.name)

        # Auto-generate meta_title and meta_description if not provided
        if not self.meta_title:
            self.meta_title = f"{self.name} | Zaco Computers"
        if not self.meta_description and self.description:
            self.meta_description = (
                self.description[:155].replace('\n', ' ')
                if len(self.description) > 155 else self.description
            )

        super().save(*args, **kwargs)


class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = RichTextField(blank=True, null=True)

    # ✅ SEO fields
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} → {self.name}"

    def save(self, *args, **kwargs):
        # Auto-generate slug if missing
        if not self.slug:
            self.slug = slugify(self.name)

        # Auto-generate meta fields if missing
        if not self.meta_title:
            self.meta_title = f"{self.name} | {self.category.name} | Zaco Computers"
        if not self.meta_description and self.description:
            self.meta_description = (
                self.description[:155].replace('\n', ' ')
                if len(self.description) > 155 else self.description
            )

        super().save(*args, **kwargs)





from django.utils.html import strip_tags
from django.utils.text import slugify

class Product(models.Model):
    category = models.ForeignKey(
        'SubCategory',
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )
    categories = models.ManyToManyField(
        'SubCategory',
        related_name='product',
        blank=True
    )

    name = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True)
    short_description = RichTextUploadingField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = ProcessedImageField(
        upload_to='products/',
        processors=[Transpose(), ResizeToFit(800, 800)],
        format='WEBP',
        options={'quality': 80},
        null=True,
        blank=True
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # SEO fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # ✅ Generate unique slug
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # ✅ Auto-fill meta title and description
        if not self.meta_title:
            self.meta_title = self.name[:255]

        # Clean HTML for meta_description
        if not self.meta_description and self.short_description:
            self.meta_description = strip_tags(self.short_description)[:500]
        else:
            self.meta_description = strip_tags(self.meta_description or "")[:500]

        # Clean short_description as well (for fallback)
        # if self.short_description:
        #     self.short_description = strip_tags(self.short_description)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', args=[self.slug])




class PPCProduct(models.Model):
    name = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    short_description = RichTextUploadingField(blank=True)
    pointer = RichTextUploadingField(blank=True)
    description = RichTextUploadingField(blank=True)

    hero_image = ProcessedImageField(
        upload_to='ppc/products/',
        processors=[Transpose(), ResizeToFit(1200, 1200)],
        format='WEBP',
        options={'quality': 85},
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    # SEO (important for landing page quality score)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while PPCProduct.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        if not self.meta_title:
            self.meta_title = self.name

        if not self.meta_description and self.short_description:
            self.meta_description = strip_tags(self.short_description)[:160]

        super().save(*args, **kwargs)



class PPCQuote(models.Model):
    product = models.ForeignKey(
        PPCProduct,
        on_delete=models.CASCADE,
        related_name="quotes"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product.name}"



class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    # Optimized gallery images
    image = ProcessedImageField(
        upload_to="products/gallery/",
        processors=[Transpose(), ResizeToFit(800, 800)],
        format='WEBP',
        options={'quality': 80},
        null=True,
        blank=True
    )

    alt_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.product.name} - Image"

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} ({self.rating}★)"





class Order(models.Model):
    # attach to a logged-in user if available (optional)
    user        = models.ForeignKey(User, null=True, blank=True,
                                    on_delete=models.SET_NULL)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    email       = models.EmailField()
    phone       = models.CharField(max_length=20)
    address     = models.TextField()
    city        = models.CharField(max_length=100)
    state       = models.CharField(max_length=100)
    zip_code    = models.CharField(max_length=15)
    country     = models.CharField(max_length=100)
    notes       = models.TextField(blank=True)
    total       = models.DecimalField(max_digits=10, decimal_places=2,
                                      default=Decimal('0.00'))
    

    # Bank Transfer Fields
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payer_name = models.CharField(max_length=100, blank=True, null=True)
    payer_bank_name = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(
        max_length=20,
        choices=(("Pending", "Pending"), ("Verified", "Verified")),
        default="Pending"
    )

    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} – {self.first_name}"
    

class OrderItem(models.Model):
    order     = models.ForeignKey(Order, related_name='items',
                                  on_delete=models.CASCADE)
    product   = models.ForeignKey('Product', on_delete=models.PROTECT)
    price     = models.DecimalField(max_digits=10, decimal_places=2)
    quantity  = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
    

# ------------------------
# Category Model
# ------------------------
class CategoryBlog(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories_blog"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ------------------------
# SubCategory Model
# ------------------------
# class SubCategoryBlog(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey('globalwebsite.CategoryBlog', on_delete=models.CASCADE, related_name='subcategories')
#     slug = models.SlugField(unique=True, blank=True)

#     class Meta:
#         verbose_name_plural = "SubCategories"
#         ordering = ['name']

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.name)
#             slug = base_slug
#             counter = 1
#             # Ensure slug is unique
#             while SubCategory.objects.filter(slug=slug).exists():
#                 slug = f"{base_slug}-{counter}"
#                 counter += 1
#             self.slug = slug
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.name} ({self.category.name})"


# ------------------------
# Tag Model
# ------------------------
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ------------------------
# Blog Model
# ------------------------
class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextUploadingField()
    category = models.ForeignKey(
        'CategoryBlog',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField('Tag', blank=True)

    # Optimized blog thumbnail
    image = ProcessedImageField(
        upload_to="blog/thumbnails/",
        processors=[Transpose(), ResizeToFit(1200, 800)],
        format='WEBP',
        options={'quality': 80},
        null=True,
        blank=True
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_desc = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog}"
