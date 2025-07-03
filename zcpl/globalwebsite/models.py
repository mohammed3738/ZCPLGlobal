from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
from django.db import models

# Create your models here.

# from django import forms

class ContactMessageGlobal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.category.name} -> {self.name}"



# class Product(models.Model):
#     category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
#     name = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     short_description = models.TextField(blank=True,null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='products/', blank=True, null=True)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

class Product(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    categories = models.ManyToManyField(SubCategory, related_name='product', blank=True, null=True)

    name = models.CharField(max_length=200)
    description = RichTextField(blank=True)
    short_description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

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
