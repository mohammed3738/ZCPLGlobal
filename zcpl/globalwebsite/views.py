from email import message
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .cart import Cart
from .forms import *
import json
import html
from django.db.models import Q, Avg
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm
# from .models import Product
from .forms import ProductForm, ShopContactForm, ContactMessageGlobalForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods

from django.db import transaction

from django.db.models import Count
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request,'main/index.html')

def about_us(request):
    return render(request,'main/about.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         name = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         # Save to database
#         ContactMessageGlobal.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message
#         )

#         full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

#         send_mail(
#             subject,
#             full_message,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_RECEIVER_EMAIL],
#             fail_silently=False,
#         )

#     else:
#         form = ContactForm()


#     return render(request,'main/contact.html',{"form": form})










def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # ✅ Validate including captcha
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Save to database
            ContactMessageGlobal.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )

            # ✅ Set session flag for thank you page access
            request.session['form_submitted'] = True  
            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})


def thank_you(request):
    # # ✅ Only allow access if session flag is set
    # if not request.session.get('form_submitted'):
    #     return redirect('/')  # or redirect('contact')

    # # Remove flag after showing once (prevents refresh hack)
    # del request.session['form_submitted']  

    return render(request, 'main/thank_you.html')


def services(request):
    return render(request,'services/services.html')


def itadservices(request):
    return render(request,'services/itad_services.html')

def it_hardware(request):
    return render(request,'services/it_hardware.html')

def server_maintenance(request):
    return render(request,'services/server_maintenance.html')

def storage_maintenance(request):
    return render(request,'services/storage_maintenance.html')

def network_maintenance(request):
    return render(request,'services/network_maintenance.html')

def rental_services(request):
    return render(request,'services/rental_services.html')

def infrastructure_service(request):
    return render(request,'services/infrastructure_service.html')

def global_it(request):
    return render(request,'services/global_it.html')

def microsoft_vm(request):
    return render(request,'services/microsoft_vm.html')


def privacy(request):
    return render(request,'main/privacy.html')


def term(request):
    return render(request,'main/terms.html')

# def shop(request):
#     products = Product.objects.all().order_by('-id')

#     return render(request,'main/shop.html', {'products': products})
# @login_required
# def add_product(request):
#     error = ""
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         category_id = request.POST.get('category')
#         short_description = request.POST.get('short_description')
#         description = request.POST.get('description')
#         available = request.POST.get('available') == 'on'
#         image = request.FILES.get('image')

#         if name and price and category_id:
#             try:
#                 category = SubCategory.objects.get(id=category_id)
#                 Product.objects.create(
#                     name=name,
#                     price=price,
#                     category=category,
#                     short_description=short_description,
#                     description=description,
#                     available=available,
#                     image=image
#                 )
#             except SubCategory.DoesNotExist:
#                 error = "Selected category does not exist."
#         else:
#             error = "Please fill in all required fields."

#     subcategories = SubCategory.objects.all()
#     products = Product.objects.all().order_by('-created')

#     return render(request, 'main/add_product.html', {
#         'subcategories': subcategories,
#         'products': products,
#         'error': error
#     })
# def product_list(request):
#     products = Product.objects.all().order_by('-id')
#     return render(request, 'shop/product_list.html', {'products': products})



# edit and add product view 
# def add_or_edit_product(request):
#     subcategories = SubCategory.objects.all()
#     products = Product.objects.all().order_by('-created')
#     error = ""
#     editing = False
#     product_to_edit = None

#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')  # for editing
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         category_id = request.POST.get('category')
#         short_description = request.POST.get('short_description')
#         description = request.POST.get('description')
#         available = request.POST.get('available') == 'on'
#         image = request.FILES.get('image')

#         try:
#             category = SubCategory.objects.get(id=category_id)
#         except SubCategory.DoesNotExist:
#             error = "Selected category does not exist."
#             category = None

#         if name and price and category:
#             if product_id:  # Update existing product
#                 product = get_object_or_404(Product, id=product_id)
#                 product.name = name
#                 product.price = price
#                 product.category = category
#                 product.short_description = short_description
#                 product.description = description
#                 product.available = available
#                 if image:
#                     product.image = image
#                 product.save()
#             else:  # Add new product
#                 Product.objects.create(
#                     name=name,
#                     price=price,
#                     category=category,
#                     short_description=short_description,
#                     description=description,
#                     available=available,
#                     image=image
#                 )
#             return redirect('add_or_edit_product')
#         else:
#             error = "Please fill in all required fields."

#     elif request.method == 'GET' and 'edit' in request.GET:
#         editing = True
#         product_id = request.GET.get('edit')
#         product_to_edit = get_object_or_404(Product, id=product_id)

#     return render(request, 'main/add_product.html', {
#         'subcategories': subcategories,
#         'products': products,
#         'editing': editing,
#         'product_to_edit': product_to_edit,
#         'error': error
#     })


from django.db.models import Q
from django.core.files.storage import FileSystemStorage

@login_required
def manage_products(request):
    editing = False
    product_to_edit = None
    error = None

    # Handle delete product
    delete_id = request.GET.get('delete')
    if delete_id:
        Product.objects.filter(id=delete_id).delete()
        return redirect('add_or_edit_product')

    # Handle edit mode
    edit_id = request.GET.get('edit')
    if edit_id:
        product_to_edit = get_object_or_404(Product, id=edit_id)
        editing = True

    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        available = True if request.POST.get('available') == 'on' else False
        short_description = request.POST.get('short_description')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # SEO fields
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')

        # Multiple category selection
        category_ids = request.POST.getlist('categories')
        selected_subcategories = SubCategory.objects.filter(id__in=category_ids)

        if not all([name, price]) or not selected_subcategories:
            error = "Name, Price, and at least one Category are required."
        else:

            if not editing:
                product = Product.objects.create(
                    name=name,
                    price=price,
                    available=available,
                    short_description=short_description,
                    description=description,
                    meta_title=meta_title,
                    meta_description=meta_description,
                )
                if image:
                    product.image = image
                    product.save()
            else:
                product = product_to_edit
                product.name = name
                product.price = price
                product.available = available
                product.short_description = short_description
                product.description = description
                product.meta_title = meta_title
                product.meta_description = meta_description

                if image:
                    product.image = image

                product.save()

            product.categories.set(selected_subcategories)

            # 🔥 Handle deleting selected gallery images
            delete_gallery = request.POST.getlist("delete_gallery")
            if delete_gallery:
                ProductImage.objects.filter(id__in=delete_gallery).delete()

            # 🔥 Handle uploading NEW gallery images
            gallery_images = request.FILES.getlist('gallery_images')
            for g_image in gallery_images:
                ProductImage.objects.create(product=product, image=g_image)

            messages.success(request, "Product updated successfully!" if editing else "Product added successfully!")
            return redirect('add_or_edit_product')

    # Fetch subcategories
    subcategories = SubCategory.objects.all()

    # Search & sorting
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', '-created')

    products = Product.objects.all()

    if search:
        products = products.filter(
            Q(name__icontains=search) |
            Q(categories__name__icontains=search)
        ).distinct()

    if sort:
        products = products.order_by(sort)

    return render(request, 'main/add_product.html', {
        'editing': editing,
        'product_to_edit': product_to_edit,
        'subcategories': subcategories,
        'products': products,
        'error': error
    })

from django.core.paginator import Paginator

# def shop(request, category_slug=None):
#     query = request.GET.get('q', '')
#     sort = request.GET.get('sort', '')
#     page_number = request.GET.get('page', 1)

#     products = Product.objects.filter(available=True)

#     if query:
#         products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     else:
#         category = None

#     if sort == 'price_asc':
#         products = products.order_by('price')
#     elif sort == 'price_desc':
#         products = products.order_by('-price')
#     elif sort == 'date':
#         products = products.order_by('-created_at')
#     elif sort == 'rating':
#         products = products.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')

#     paginator = Paginator(products, 9)  # 9 products per page
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'main/shop.html', {
#         'category': category,
#         'categories': Category.objects.all(),
#         'products': page_obj
#     })

# views.py

def shop(request, category_slug=None, subcategory_slug=None):
    query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    page_number = request.GET.get('page', 1)

    products = Product.objects.filter(available=True)

    category = None
    subcategory = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = SubCategory.objects.filter(category=category)

        if subcategory_slug:
            subcategory = get_object_or_404(SubCategory, slug=subcategory_slug, category=category)
            products = products.filter(categories=subcategory)
        else:
            products = products.filter(categories__in=subcategories)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'date':
        products = products.order_by('-created_at')
    elif sort == 'rating':
        products = products.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating')

    paginator = Paginator(products, 9)
    page_obj = paginator.get_page(page_number)

    # Contact form handling
    contact_form = ShopContactForm()
    contact_success = False

    if request.method == 'POST' and 'contact_form_submit' in request.POST:
        contact_form = ShopContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()  # Save to ContactMessageGlobal model
            
            cd = contact_form.cleaned_data
            full_message = f"Name: {cd['name']}\nEmail: {cd['email']}\nPhone: {cd['phone']}\n\nMessage:\n{cd['message']}"
            
            send_mail(
                cd['subject'],
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
            
            contact_success = True
            return redirect('thank_you')

    return render(request, 'main/shop.html', {
        'category': category,
        'subcategory': subcategory,
        'products': page_obj,
        'categories': Category.objects.all(),
        'contact_form': contact_form,
        'contact_success': contact_success,
    })

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart_detail')



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'main/cart_detail.html', {'cart': cart})
def cart_detail(request):
    cart = Cart(request)
    cart_items = list(cart)  # turn generator into list for pagination
    paginator = Paginator(cart_items, 5)  # 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main/cart.html', {
        'cart': cart,
        'cart_page_obj': page_obj,
    })




# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'main/product_detail.html', {
#         'product': product,
#         'cart_product_form': cart_product_form
#     })
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     reviews = product.reviews.all().order_by('-created_at')
#     cart_product_form = CartAddProductForm()
    
#     if request.method == 'POST':
#         review_form = ReviewForm(request.POST)
#         if review_form.is_valid():
#             review = review_form.save(commit=False)
#             review.product = product
#             review.save()
#             return redirect('product_detail', product_id=product.id)
#     else:
#         review_form = ReviewForm()

#     return render(request, 'main/product_detail.html', {
#         'product': product,
#         'cart_product_form': cart_product_form,
#         'review_form': review_form,
#         'reviews': reviews
#     })



# ---------- Helpers ----------

def clean_text_for_jsonld(text, max_chars=500):
    """
    - strip HTML tags
    - unescape HTML entities (&nbsp;, &amp;, etc.)
    - replace CR/LF and NBSP with spaces
    - collapse multiple spaces and truncate
    """
    if not text:
        return ""
    # remove tags
    t = strip_tags(text)
    # unescape HTML entities (turn &nbsp; -> non-breaking space, &amp; -> &)
    t = html.unescape(t)
    # replace NBSP and other Unicode non-breaking spaces with normal space
    t = t.replace('\u00A0', ' ')
    # replace CR/LF/tabs with space
    t = t.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    # collapse multiple spaces
    t = ' '.join(t.split())
    if max_chars:
        return t[:max_chars].strip()
    return t.strip()

KNOWN_BRANDS = ["DELL", "HPE", "IBM", "CISCO"]

def extract_brand_token_from_text(text, known_brands=None):
    if not text:
        return None
    if known_brands is None:
        known_brands = KNOWN_BRANDS
    txt = text.strip().upper()
    for b in known_brands:
        if txt == b or txt.startswith(b + " ") or f" {b} " in f" {txt} ":
            return b
    return None

def derive_brand_using_subcategory_category(product):
    """
    1) product.brand.name (if exists)
    2) product.category.category.name (subcategory -> category)
    3) product.category.name (subcategory)
    4) product.name (scan)
    5) fallback Generic
    """
    # 1) explicit brand
    try:
        if hasattr(product, 'brand') and getattr(product, 'brand') is not None:
            brand_obj = getattr(product, 'brand')
            if hasattr(brand_obj, 'name') and brand_obj.name:
                bn = str(brand_obj.name).strip()
                if bn:
                    return bn
    except Exception:
        pass

    # 2) subcategory -> category
    try:
        subcat = getattr(product, 'category', None)
        if subcat is not None:
            parent_cat = getattr(subcat, 'category', None)
            if parent_cat is not None:
                parent_name = getattr(parent_cat, 'name', None) or ""
                tok = extract_brand_token_from_text(parent_name)
                if tok:
                    return tok
            # 3) subcategory name
            subcat_name = getattr(subcat, 'name', None) or ""
            tok = extract_brand_token_from_text(subcat_name)
            if tok:
                return tok
    except Exception:
        pass

    # 4) product name
    try:
        pnm = getattr(product, 'name', '') or ''
        tok = extract_brand_token_from_text(pnm)
        if tok:
            return tok
    except Exception:
        pass

    return "Generic"

def build_jsonld_dicts(request, product):
    """
    Build Product and Breadcrumb JSON-LD dicts and return them.
    """
    base = f"{request.scheme}://{request.get_host()}"

    # description cleaned (removes &nbsp; etc.)
    desc = ""
    if hasattr(product, 'meta_description') and product.meta_description:
        desc = clean_text_for_jsonld(product.meta_description, 500)
    else:
        desc = clean_text_for_jsonld(getattr(product, 'short_description', ''), 500)

    # images absolute urls
    images = []
    if hasattr(product, 'image') and getattr(product, 'image', None):
        try:
            images.append(f"{base}{product.image.url}")
        except Exception:
            pass
    if hasattr(product, 'images') and getattr(product, 'images', None) is not None:
        try:
            for img in product.images.all():
                if getattr(img, 'image', None):
                    try:
                        images.append(f"{base}{img.image.url}")
                    except Exception:
                        continue
        except Exception:
            pass

    # brand resolution
    jsonld_brand = derive_brand_using_subcategory_category(product)

    # price only if numeric > 0
    jsonld_price = None
    if hasattr(product, 'price') and product.price not in (None, ''):
        try:
            p = Decimal(product.price)
            if p > 0:
                jsonld_price = float(p)
        except Exception:
            jsonld_price = None

    # Product dict
    product_ld = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": strip_tags(getattr(product, 'name', '') or ""),
        "image": images,
        "description": desc,
        "brand": {
            "@type": "Brand",
            "name": jsonld_brand
        }
    }

    if jsonld_price is not None:
        product_ld["offers"] = {
            "@type": "Offer",
            "url": request.build_absolute_uri(),
            "priceCurrency": "INR",
            "price": jsonld_price,
            "availability": "https://schema.org/InStock" if getattr(product, 'available', True) else "https://schema.org/OutOfStock",
            "seller": {
                "@type": "Organization",
                "name": "Zaco Computers Pvt. Ltd."
            }
        }

    # Breadcrumbs (subcategory -> product)
    breadcrumb_items = [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{base}/"},
        {"@type": "ListItem", "position": 2, "name": "Shop", "item": f"{base}/shop/"},
    ]
    try:
        subcat = getattr(product, 'category', None)
        if subcat is not None and getattr(subcat, 'name', None):
            breadcrumb_items.append({"@type": "ListItem", "position": 3, "name": subcat.name, "item": f"{base}/shop/{getattr(subcat, 'slug', '')}/"})
            breadcrumb_items.append({"@type": "ListItem", "position": 4, "name": strip_tags(getattr(product, 'name', '')), "item": request.build_absolute_uri()})
        else:
            breadcrumb_items.append({"@type": "ListItem", "position": 3, "name": strip_tags(getattr(product, 'name', '')), "item": request.build_absolute_uri()})
    except Exception:
        breadcrumb_items.append({"@type": "ListItem", "position": 3, "name": strip_tags(getattr(product, 'name', '')), "item": request.build_absolute_uri()})

    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumb_items
    }

    return product_ld, breadcrumb_ld
# ---------- View ----------

# def product_detail(request, slug):
#     """
#     Full product_detail view.
#     Adjust forms and models import names if your project differs.
#     """
#     product = get_object_or_404(Product, slug=slug)
#     SERVER_RENTABLE_CATEGORIES = [
#         "DELL RACK SERVER", "DELL TOWER SERVER", "DELL BLADE SERVER",
#         "HPE RACK SERVER", "HPE TOWER SERVER", "HPE BLADE SERVER",
#         "IBM RACK SERVER", "IBM TOWER SERVER", "IBM BLADE SERVER",
#     ]

#     print(product.subcategory.upper())
#     show_rent_button = False
#     # try:
#         if product.subcategory.upper() in SERVER_RENTABLE_CATEGORIES:
#             show_rent_button = True
#     # except:
#     #     pass

#     # Reviews & pagination (defensive)
#     reviews_qs = product.reviews.all().order_by('-created_at') if hasattr(product, 'reviews') else []
#     paginator = Paginator(reviews_qs, 8) if reviews_qs else None
#     page_num = request.GET.get('page', 1)
#     if paginator:
#         try:
#             reviews = paginator.page(page_num)
#         except:
#             reviews = paginator.page(1)
#     else:
#         reviews = []

#     review_count = reviews_qs.count() if reviews_qs else 0
#     avg_rating = reviews_qs.aggregate(avg=Avg('rating'))['avg'] if reviews_qs else 0
#     try:
#         avg_rating = round(float(avg_rating), 2) if avg_rating else 0.0
#     except Exception:
#         avg_rating = 0.0

#     # Forms
#     cart_product_form = CartAddProductForm()
#     contact_form = ShopContactForm()

#     # POST handling: review or quote
#     if request.method == 'POST':
#         # Review submit
#         if 'comment' in request.POST and 'rating' in request.POST:
#             name = request.POST.get('name', '').strip()
#             comment = request.POST.get('comment', '').strip()
#             try:
#                 rating = int(request.POST.get('rating', '0'))
#             except Exception:
#                 rating = None

#             if name and comment and rating:
#                 rating = max(1, min(5, rating))
#                 try:
#                     with transaction.atomic():
#                         Review.objects.create(product=product, name=name, comment=comment, rating=rating)
#                     messages.success(request, "Thank you for your review!")
#                     return redirect('product_detail', slug=slug)
#                 except Exception as e:
#                     messages.error(request, "Could not save review: " + str(e))
#             else:
#                 messages.error(request, "Please provide name, comment and rating.")

#         # Quote form submit
#         elif 'email' in request.POST and 'message' in request.POST:
#             contact_form = ShopContactForm(request.POST)
#             if contact_form.is_valid():
#                 # Save form and get the instance
#                 obj = contact_form.save()
#                 print("Quote request saved to database.", contact_form.cleaned_data)

#                 # Prepare email using the saved instance
#                 subject = f"New Quote Request from {obj.name}"
#                 message = (
#                     f"You received a new quote request.\n\n"
#                     f"Name: {obj.name}\n"
#                     f"Email: {obj.email}\n"
#                     f"Phone: {obj.phone}\n"
#                     f"Company: {obj.subject}\n"
#                     f"Message:\n{obj.message}\n\n"
#                     f"Submitted At: {obj.submitted_at}"
#                 )

#                 from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@zacocomputer.com")
#                 to_emails = ["info@zacocomputer.com"]

#                 try:
#                     send_mail(
#                         subject,
#                         message,
#                         from_email,
#                         to_emails,
#                         fail_silently=False,
#                     )
#                     print("Quote Email Sent Successfully.")
#                 except Exception as e:
#                     print("Error sending quote email:", e)

#                 # Success message and redirect
#                 messages.success(request, "Your quote request has been sent!")
#                 return redirect('thank_you')

#             else:
#                 messages.error(request, "Please fix errors in the quote form.")

#     # Meta fallbacks
#     meta_title = product.meta_title if hasattr(product, 'meta_title') and product.meta_title else getattr(product, 'name', '')
#     if hasattr(product, 'meta_description') and product.meta_description:
#         meta_description = clean_text_for_jsonld(product.meta_description, 500)
#     else:
#         meta_description = clean_text_for_jsonld(getattr(product, 'short_description', ''), 500)

#     # Build JSON-LD dicts and dump to strings (prevent \u escapes)
#     product_ld, breadcrumb_ld = build_jsonld_dicts(request, product)
#     product_jsonld_str = json.dumps(product_ld, ensure_ascii=False, indent=2)
#     breadcrumb_jsonld_str = json.dumps(breadcrumb_ld, ensure_ascii=False, indent=2)

#     context = {
#         'product': product,
#         'cart_product_form': cart_product_form,
#         'contact_form': contact_form,
#         'reviews': reviews,
#         'review_count': review_count,
#         'avg_rating': avg_rating,
#         'meta_title': meta_title,
#         'meta_description': meta_description,
#         'product_jsonld': product_jsonld_str,
#         'breadcrumb_jsonld': breadcrumb_jsonld_str,
#         'show_rent_button': show_rent_button,
#     }

#     return render(request, 'main/product_detail.html', context)



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # ---------------------------------------------
    # RENTABLE CATEGORIES
    # ---------------------------------------------
    SERVER_RENTABLE_CATEGORIES = [
        "DELL RACK SERVER", "DELL TOWER SERVER", "DELL BLADE SERVER",
        "HPE RACK SERVER", "HPE TOWER SERVER", "HPE BLADE SERVER",
        "IBM RACK SERVER", "IBM TOWER SERVER", "IBM BLADE SERVER",
    ]

    show_rent_button = False
    try:
        if product.category.name.upper() in SERVER_RENTABLE_CATEGORIES:
            show_rent_button = True
    except:
        pass

    # ---------------------------------------------
    # Reviews & forms
    # ---------------------------------------------
    reviews_qs = product.reviews.all().order_by("-created_at")
    paginator = Paginator(reviews_qs, 8)
    page_num = request.GET.get("page", 1)

    try:
        reviews = paginator.page(page_num)
    except:
        reviews = paginator.page(1)

    review_count = reviews_qs.count()
    avg_rating = reviews_qs.aggregate(avg=Avg("rating"))["avg"] or 0

    try:
        avg_rating = round(float(avg_rating), 2)
    except:
        avg_rating = 0

    cart_product_form = CartAddProductForm()
    contact_form = ShopContactForm()
    rent_form = ShopContactForm()

    # --------------------------------------------------
    # HANDLE RENT REQUEST FORM
    # --------------------------------------------------
    if request.method == "POST" and "rent_request" in request.POST:
        rent_form = ShopContactForm(request.POST)
        if rent_form.is_valid():
            obj = rent_form.save(commit=False)
            obj.subject = f"Rent Request for {product.name}"
            obj.save()

            subject = obj.subject
            message = (
                f"Rent Request for Product: {product.name}\n\n"
                f"Name: {obj.name}\n"
                f"Email: {obj.email}\n"
                f"Phone: {obj.phone}\n\n"
                f"Message:\n{obj.message}\n\n"
                f"Submitted At: {obj.submitted_at}"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["info@zacocomputer.com"],
                fail_silently=False,
            )

            return redirect("thank_you")

    # --------------------------------------------------
    # HANDLE QUOTE REQUEST FORM
    # --------------------------------------------------
    if request.method == "POST" and "quote_request" in request.POST:
        contact_form = ShopContactForm(request.POST)
        if contact_form.is_valid():
            obj = contact_form.save()

            subject = f"New Quote Request for {product.name}"
            message = (
                f"Quote Request for Product: {product.name}\n\n"
                f"Name: {obj.name}\n"
                f"Email: {obj.email}\n"
                f"Phone: {obj.phone}\n"
                f"Company: {obj.subject}\n\n"
                f"Message:\n{obj.message}"
            )

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["info@zacocomputer.com"],
                fail_silently=False,
            )

            return redirect("thank_you")

    # --------------------------------------------------
    # JSON-LD
    # --------------------------------------------------
    product_ld, breadcrumb_ld = build_jsonld_dicts(request, product)
    product_jsonld = json.dumps(product_ld, ensure_ascii=False)
    breadcrumb_jsonld = json.dumps(breadcrumb_ld, ensure_ascii=False)

    # --------------------------------------------------
    # CONTEXT
    # --------------------------------------------------
    context = {
        "product": product,
        "reviews": reviews,
        "review_count": review_count,
        "avg_rating": avg_rating,
        "cart_product_form": cart_product_form,
        "contact_form": contact_form,
        "rent_form": rent_form,
        "show_rent_button": show_rent_button,
        "product_jsonld": product_jsonld,
        "breadcrumb_jsonld": breadcrumb_jsonld,
    }

    return render(request, "main/product_detail.html", context)




def cart_update_all(request):
    cart = Cart(request)
    for key, value in request.POST.items():
        if key.startswith('quantity_'):
            try:
                product_id = key.split('_')[1]
                product = Product.objects.get(id=product_id)
                quantity = int(value)
                cart.add(product=product, quantity=quantity, override_quantity=True)
            except (Product.DoesNotExist, ValueError):
                continue
    return redirect('cart_detail')




# @login_required
# def checkout(request):
#     cart = Cart(request)
#     if len(cart) == 0:          # cart empty → kick back to shop
#         messages.info(request, "Your cart is empty.")
#         return redirect('shop')  # adjust if your shop URL name differs

#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             order = Order.objects.create(
#                 user       = request.user if request.user.is_authenticated else None,
#                 first_name = data['first_name'],
#                 last_name  = data['last_name'],
#                 email      = data['email'],
#                 phone      = data['phone'],
#                 address    = data['address'],
#                 city       = data['city'],
#                 state      = data['state'],
#                 zip_code   = data['zip_code'],
#                 country    = data['country'],
#                 notes      = data.get('notes',''),
#                 total      = cart.get_total_price()
#             )
#             for item in cart:          # cart.__iter__() provides product, qty…
#                 OrderItem.objects.create(
#                     order    = order,
#                     product  = item['product'],
#                     price    = item['product'].price,
#                     quantity = item['quantity']
#                 )
#             cart.clear()               # empty session cart
#             return redirect('order_success', order_id=order.id)
#     else:
#         form = CheckoutForm()

#     return render(request, 'main/checkout1.html',
#                   {'form': form, 'cart': cart})



#second working
# def checkout(request):
#     cart = Cart(request)

#     if len(cart) == 0:
#         messages.info(request, "Your cart is empty.")
#         return redirect('shop')  # or whatever your shop URL name is

#     if request.method == "POST":
#         form = BankTransferForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             order = Order.objects.create(
#                 user=request.user if request.user.is_authenticated else None,
#                 first_name=cd['first_name'],
#                 last_name=cd['last_name'],
#                 email=cd['email'],
#                 phone=cd['phone'],
#                 address=cd['address'],
#                 city=cd['city'],
#                 state=cd['state'],
#                 zip_code=cd['zip_code'],
#                 country=cd['country'],
#                 transaction_id=cd['transaction_id'],
#                 payer_name=cd['payer_name'],
#                 payer_bank_name=cd['payer_bank_name'],
#                 payment_status="Pending",
#                 total=cart.get_total_price()
#             )

#             for item in cart:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item['product'],
#                     price=item['product'].price,
#                     quantity=item['quantity']
#                 )

#             cart.clear()
#             return redirect('order_success', order_id=order.id)

#     else:
#         form = BankTransferForm()

#     # Sample company bank details
#     bank_info = {
#         "account_name": "Zaco Computers Pvt Ltd",
#         "account_number": "1234567890",
#         "ifsc": "HDFC0001234",
#         "bank_name": "HDFC Bank",
#         "branch": "Mumbai Main Branch"
#     }

#     return render(request, "main/checkout2.html", {
#         "form": form,
#         "cart": cart,
#         "bank_info": bank_info
#     })




@login_required
def checkout(request):
    cart = Cart(request)

    if request.method == "POST":
        form = BankTransferForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(
                user=request.user,
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                address=cd['address'],
                city=cd['city'],
                state=cd['state'],
                zip_code=cd['zip_code'],
                country=cd['country'],
                phone=cd['phone'],
                email=cd['email'],
                transaction_id=cd['transaction_id'],
                payer_name=cd['payer_name'],
                payer_bank_name=cd['payer_bank_name'],
                payment_status="Pending"
            )

            # Email admin
            subject = f"New Order #{order.id} Received"
            message = f"""
A new order has been placed.

Order ID: {order.id}
Customer: {order.first_name} {order.last_name}
Email: {order.email}
Phone: {order.phone}
Transaction ID: {order.transaction_id}
Amount: ₹{cart.get_total_price()}

Please verify the payment and process the order.
"""
            admin_email = 'admin@example.com'  # replace with your admin email
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [admin_email])

            cart.clear()
            return render(request, "main/order_success.html", {"order": order})
    else:
        form = BankTransferForm()

    bank_info = {
        "account_name": "Zaco Computers Pvt Ltd",
        "account_number": "1234567890",
        "ifsc": "HDFC0001234",
        "bank_name": "HDFC Bank",
        "branch": "Mumbai Main Branch"
    }

    return render(request, "main/checkout2.html", {
        "form": form,
        "cart": cart,
        "bank_info": bank_info
    })




def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'main/order_success.html', {'order': order})





def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validations
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)  # Optional: auto-login
        messages.success(request, "Account created successfully!")
        return redirect('home')  # Update to your desired redirect

    return render(request, 'auth/register.html')



# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])  # hashes password
#             user.save()
#             login(request, user)
#             return redirect('shop')  # change to your landing page
#     else:
#         form = SignUpForm()
#     return render(request, 'auth/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('signin')


# Blog List View
def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    categories = CategoryBlog.objects.annotate(num_posts=Count('blog'))
    # sub_categories = SubCategoryBlog.objects.annotate(num_posts=Count('blog'))
    tags = Tag.objects.all()
    archives = Blog.objects.dates('created_at', 'month', order='DESC')

    context = {
        'blogs': blogs,
        'categories_blog': categories,
        'tags': tags,
        'archives': archives,
    }
    return render(request, 'blog/blog_list.html', context)

# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             form.save_m2m()
#             return redirect('blog_list')
#     else:
#         form = BlogForm()
#     return render(request, 'blog/create_blog.html', {'form': form})

# def blog_detail(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     return render(request, 'blog/blog_detail.html', {'blog': blog})

# def blog_detail(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)
#     comments = blog.comments.all().order_by('-created_at')  # latest first

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.blog = blog
#             comment.user = request.user  # make sure user is logged in
#             comment.save()
#             return redirect('blog_detail', slug=blog.slug)
#     else:
#         form = CommentForm()

#     context = {
#         'blog': blog,
#         'comments': comments,
#         'form': form
#     }
#     return render(request, 'blog/blog_detail.html', context)


# @login_required
# def add_blog(request):
#     if request.method == "POST":
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user
#             blog.save()
#             form.save_m2m()  # Save tags
#             return redirect("blog_detail", slug=blog.slug)
#     else:
#         form = BlogForm()
#     return render(request, "blog/create_blog.html", {"form": form})



def blogs_by_category(request, slug):
    category = get_object_or_404(CategoryBlog, slug=slug)
    blogs = Blog.objects.filter(category=category)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'selected_category': category})

# def blogs_by_subcategory(request, slug):
#     subcategory = get_object_or_404(SubCategoryBlog, slug=slug)
#     blogs = Blog.objects.filter(sub_category=subcategory)
#     return render(request, 'blog/blog_list.html', {'blogs': blogs, 'selected_subcategory': subcategory})


def blogs_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    blogs = Blog.objects.filter(tags=tag)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'selected_tag': tag})

def blogs_by_archive(request, year, month):
    blogs = Blog.objects.filter(created_at__year=year, created_at__month=month)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'archive_date': f"{month}-{year}"})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all().order_by('-created_at')
    latest_posts = Blog.objects.order_by("-created_at")[:3]  # for sidebar

    # Sidebar data
    categories = CategoryBlog.objects.annotate(num_posts=Count('blog'))
    tags = Tag.objects.all()
    archives = Blog.objects.dates('created_at', 'month', order='DESC')

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = CommentForm()

    return render(request, "blog/blog_detail.html", {
        "blog": blog,
        "comments": comments,
        "form": form,
        "latest_posts": latest_posts,
        "categories_blog": categories,
        "tags": tags,
        "archives": archives,
    })



# @login_required
# def manage_blogs(request):
#     editing = False
#     blog_to_edit = None
#     error = None

#     # ----- Edit Blog -----
#     if "edit" in request.GET:
#         editing = True
#         blog_to_edit = get_object_or_404(Blog, id=request.GET.get("edit"))

#         if request.method == "POST":
#             form = BlogForm(request.POST, request.FILES, instance=blog_to_edit)
#             if form.is_valid():
#                 blog = form.save(commit=False)
#                 blog.author = request.user  # keep current author
#                 blog.save()
#                 form.save_m2m()  # save tags
#                 return redirect("blog_detail", slug=blog.slug)
#             else:
#                 error = "Please correct the errors below."
#         else:
#             form = BlogForm(instance=blog_to_edit)

#     # ----- Delete Blog -----
#     elif "delete" in request.GET:
#         blog = get_object_or_404(Blog, id=request.GET.get("delete"))
#         blog.delete()
#         return redirect("blog_detail", slug=blog.slug)
#     # ----- Add Blog -----
#     else:
#         if request.method == "POST":
#             form = BlogForm(request.POST, request.FILES)
#             if form.is_valid():
#                 blog = form.save(commit=False)
#                 blog.author = request.user  # set author
#                 blog.save()
#                 form.save_m2m()
#                 return redirect("blog_detail", slug=blog.slug)
#             else:
#                 error = "Please correct the errors below."
#         else:
#             form = BlogForm()

#     # ----- Blog List -----
#     blogs = Blog.objects.all()
#     categories = CategoryBlog.objects.all()
#     tags = Tag.objects.all()

#     return render(request, "blog/create_blog.html", {
#         "form": form,
#         "blogs": blogs,
#         "categories": categories,
#         "tags": tags,
#         "editing": editing,
#         "blog_to_edit": blog_to_edit,
#         "error": error,
#     })

@login_required
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user if request.user.is_authenticated else None
            blog.save()
            form.save_m2m()  # save tags/categories relations
            messages.success(request, "Blog added successfully!")
            return redirect("blog_list")  # change this to your blog list URL name
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BlogForm()

    return render(request, "blog/create_blog.html", {"form": form})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully!")
            return redirect("blog_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BlogForm(instance=blog)

    return render(request, "blog/create_blog.html", {"form": form, "editing": True})



# def sitemap(request):
#     return render(request,'sitemap.xml', content_type="application/xml")

def robots_txt(request):
    return render(request,'robots.txt', content_type="text/plain")




@login_required
def category_manager(request, category_id=None):
    if category_id:
        instance = get_object_or_404(Category, id=category_id)
        form = CategoryForm(request.POST or None, instance=instance)
    else:
        instance = None
        form = CategoryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        category = form.save(commit=False)
        # Auto-fill meta title and description if empty
        if not category.meta_title:
            category.meta_title = category.name
        if not category.meta_description:
            category.meta_description = category.description[:160]  # First 160 chars
        category.save()
        return redirect('category_manager')

    categories = Category.objects.all()
    return render(request, 'main/category_manager.html', {
        'form': form,
        'categories': categories,
        'editing': category_id is not None,
    })


@login_required
def subcategory_manager(request, subcategory_id=None):
    if subcategory_id:
        instance = get_object_or_404(SubCategory, id=subcategory_id)
        form = SubCategoryForm(request.POST or None, instance=instance)
    else:
        instance = None
        form = SubCategoryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        subcategory = form.save(commit=False)
        # Auto-fill meta title and description if empty
        if not subcategory.meta_title:
            subcategory.meta_title = f"{subcategory.name} | {subcategory.category.name}"
        if not subcategory.meta_description:
            subcategory.meta_description = subcategory.description[:160]  # First 160 chars
        subcategory.save()
        return redirect('subcategory_manager')

    subcategories = SubCategory.objects.select_related('category').all()
    return render(request, 'main/subcategory_manager.html', {
        'form': form,
        'subcategories': subcategories,
        'editing': subcategory_id is not None,
    })





def google_xml_feed(request):
    response = HttpResponse(content_type="application/xml")
    response.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    response.write('<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n')
    response.write('<channel>\n')
    response.write('<title>Zaco Computers Product Feed</title>\n')
    response.write('<link>https://www.zacocomputer.com</link>\n')
    response.write('<description>Live product feed for Google Merchant Center</description>\n')

    products = Product.objects.filter(available=True)

    for product in products:

        response.write("<item>\n")

        response.write(f"<g:id>{product.id}</g:id>\n")
        response.write(f"<title><![CDATA[{product.name}]]></title>\n")

        description = strip_tags(product.meta_description or product.short_description or product.description)
        response.write(f"<description><![CDATA[{description}]]></description>\n")

        response.write(f"<link>https://www.zacocomputer.com/{product.get_absolute_url()}</link>\n")

        if product.image:
            response.write(f"<g:image_link>https://www.zacocomputer.com/{product.image.url}</g:image_link>\n")

        response.write(f"<g:condition>new</g:condition>\n")
        response.write(f"<g:availability>{'in stock' if product.available else 'out of stock'}</g:availability>\n")
        response.write(f"<g:price>{product.price} INR</g:price>\n")

        # Optional recommended values
        response.write("<g:brand>Zaco Computers</g:brand>\n")
        response.write(f"<g:product_type>{product.category}</g:product_type>\n")

        response.write("</item>\n")

    response.write("</channel>\n</rss>")

    return response




# @require_POST
# def request_quote_api(request):
#     """
#     Handle AJAX submission from the fixed 'Request Quote' drawer.
#     Saves ContactMessageGlobal and emails abhiraj@zacocomputer.com.
#     Returns JSON.
#     """
#     form = ContactMessageGlobalForm(request.POST)
#     if form.is_valid():
#         obj = form.save()

#         # Build email
#         subject = f"New Quote Request from {obj.name}"
#         message = (
#             "You have received a new quote request from the website.\n\n"
#             f"Name: {obj.name}\n"
#             f"Email: {obj.email}\n"
#             f"Phone: {obj.phone}\n"
#             f"Company: {obj.subject}\n\n"
#             f"Message:\n{obj.message}\n\n"
#             f"Submitted at: {obj.submitted_at}\n"
#         )

#         from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@zacocomputer.com")
#         to_emails = ["abhiraj@zacocomputer.com"]

#         try:
#             send_mail(
#                 subject=subject,
#                 message=message,
#                 from_email=from_email,
#                 recipient_list=to_emails,
#                 fail_silently=False,
#             )
#         except Exception as e:
#             # Log or print the error – but still return success to user
#             print("Error sending quote email:", e)

#         return JsonResponse({"success": True})

#     # Form invalid
#     return JsonResponse({"success": False, "errors": form.errors}, status=400)


import logging


logger = logging.getLogger(__name__)

@require_POST
def request_quote_api(request):
    form = ContactMessageGlobalForm(request.POST)
    if not form.is_valid():
        # Return form errors to client for display/handling
        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    obj = form.save()

    # Build email
    subject = f"New Quote Request from {obj.name}"
    message = (
        "You have received a new quote request from the website.\n\n"
        f"Name: {obj.name}\n"
        f"Email: {obj.email}\n"
        f"Phone: {obj.phone}\n"
        f"Company: {obj.subject}\n\n"
        f"Message:\n{obj.message}\n\n"
        f"Submitted at: {obj.submitted_at}\n"
        f"Source URL: {request.META.get('HTTP_REFERER', 'unknown')}\n"
    )

    # Determine recipients
    primary = getattr(settings, "CONTACT_RECEIVER_EMAIL", None) or getattr(settings, "DEFAULT_FROM_EMAIL", None)
    recipients = []
    if primary:
        recipients.append(primary)
    # add abhiraj as requested
    recipients.append("info@zacocomputer.com")

    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None) or settings.EMAIL_HOST_USER

    # Try sending mail; don't fail the request if email has issues
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipients,
            fail_silently=False,
        )
    except Exception as e:
        # Log the error so it can be investigated
        logger.exception("Error sending quote notification email for ContactMessageGlobal id=%s: %s", obj.id, e)

    # Return absolute redirect URL (client will redirect)
    redirect_url = request.build_absolute_uri(reverse("thank_you"))

    return JsonResponse({
        "success": True,
        "redirect_url": redirect_url
    })



def custom_404(request, exception=None):
    recommended = Product.objects.filter(available=True).order_by("?")[:4]

    return render(request, "404.html", {"recommended": recommended}, status=404)



def ajax_product_search(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )[:8]

        results = [
            {
                "name": p.name,
                "url": p.get_absolute_url(),
                "image": p.image.url if p.image else None
            }
            for p in products
        ]

    return JsonResponse({"results": results})





def sitemap_index(request):
    base = request.build_absolute_uri("/")[:-1]

    sitemaps = [
        f"{base}/sitemap-main.xml",
        f"{base}/sitemap-products.xml",
        f"{base}/sitemap-case-studies.xml",
        f"{base}/sitemap-blogs.xml",
        f"{base}/sitemap-india.xml",
        f"{base}/sitemap-uae.xml",
        f"{base}/sitemap-uk.xml",
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for sm in sitemaps:
        xml.append(f"""
        <sitemap>
            <loc>{sm}</loc>
        </sitemap>
        """)

    xml.append("</sitemapindex>")

    return HttpResponse("".join(xml), content_type="application/xml")




from django.core.mail import send_mail
from django.conf import settings

def ppc_product_detail(request, slug):
    product = get_object_or_404(PPCProduct, slug=slug, is_active=True)

    if request.method == "POST":
        form = PPCQuoteForm(request.POST)
        if form.is_valid():

            quote = PPCQuote.objects.create(
                product=product,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                company=form.cleaned_data["company"],
                message=form.cleaned_data["requirements"],
            )

            # -------- EMAIL CONTENT --------
            subject = f"New Quote Request – {product.name}"
            message = f"""
New Quote Request Received

Product: {product.name}

Name: {quote.name}
Email: {quote.email}
Phone: {quote.phone}
Company: {quote.company}

Requirement:
{quote.message}
"""

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["info@zacocomputer.com"],
                fail_silently=False,
            )

            return redirect("thank_you")
    else:
        form = PPCQuoteForm()

    return render(
        request,
        "ppc/product_detail.html",
        {
            "product": product,
            "form": form,
        }
    )



def ppc_product_manage(request):
    editing = False
    product_to_edit = None

    # -----------------------
    # DELETE (GET)
    # -----------------------
    delete_id = request.GET.get('delete')
    if delete_id:
        product = get_object_or_404(PPCProduct, id=delete_id)
        product.delete()
        return redirect('ppc-product-manage')

    # -----------------------
    # EDIT MODE (GET)
    # -----------------------
    edit_id = request.GET.get('edit')
    if edit_id:
        product_to_edit = get_object_or_404(PPCProduct, id=edit_id)
        editing = True

    # -----------------------
    # CREATE / UPDATE (POST)
    # -----------------------
    if request.method == "POST":
        product_id = request.POST.get('product_id')

        if product_id:
            product = get_object_or_404(PPCProduct, id=product_id)
            editing = True
        else:
            product = PPCProduct()

        product.name = request.POST.get('name')
        product.sub_heading = request.POST.get('sub_heading')
        product.price = request.POST.get('price')
        product.is_active = True if request.POST.get('is_active') == 'on' else False

        product.short_description = request.POST.get('short_description')
        product.pointer = request.POST.get('pointer')
        product.description = request.POST.get('description')

        product.meta_title = request.POST.get('meta_title')
        product.meta_description = request.POST.get('meta_description')

        if request.FILES.get('hero_image'):
            product.hero_image = request.FILES.get('hero_image')

        product.save()
        return redirect('ppc-product-manage')

    products = PPCProduct.objects.all().order_by('-created_at')

    return render(request, 'ppc/product_manage.html', {
        'products': products,
        'editing': editing,
        'product_to_edit': product_to_edit,
    })


def ppc_product_delete(request, pk):
    product = get_object_or_404(PPCProduct, pk=pk)
    product.delete()
    return redirect('ppc-product-manage')




@require_http_methods(["GET", "POST"])
def build_your_server(request):

    if request.method == "POST":

        # ============================
        # Required fields
        # ============================
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()

        if not name or not email or not phone:
            messages.error(request, "Name, Email and Phone are required.")
            return redirect("build_your_server")

        # ============================
        # Helper
        # ============================
        def g(key):
            return request.POST.get(key, "").strip()

        # ============================
        # Core selections
        # ============================
        server_brand = g("server_brand")
        server_type = g("server_type")
        form_factor = g("form_factor")
        server_model = g("server_model")

        processor = g("processor")
        memory = g("memory")
        ethernet_card = g("ethernet_card")
        server_purpose = g("server_purpose")
        additional_requirement = g("additional_requirement")

        # ============================
        # Dynamic rows
        # ============================
        ssd_list = request.POST.getlist("ssd[]")
        ssd_qty_list = request.POST.getlist("ssd_qty[]")

        hdd_list = request.POST.getlist("hdd[]")
        hdd_qty_list = request.POST.getlist("hdd_qty[]")

        other_components = request.POST.getlist("other_components[]")

        # ============================
        # Build message
        # ============================
        lines = [
            "BUILD YOUR OWN SERVER REQUEST",
            "-----------------------------------",
            f"Server Brand: {server_brand}",
            f"Server Type: {server_type}",
            f"Form Factor: {form_factor}",
            f"Server Model: {server_model}",
            "",
            f"Processor: {processor}",
            f"Memory: {memory}",
            "",
            "SSD Configuration:",
        ]

        if ssd_list:
            for ssd, qty in zip(ssd_list, ssd_qty_list):
                if ssd:
                    lines.append(f"- {ssd} × {qty or '1'}")
        else:
            lines.append("- None")

        lines.append("")
        lines.append("HDD Configuration:")

        if hdd_list:
            for hdd, qty in zip(hdd_list, hdd_qty_list):
                if hdd:
                    lines.append(f"- {hdd} × {qty or '1'}")
        else:
            lines.append("- None")

        lines.append("")
        lines.append("Other Components:")

        if other_components:
            for comp in other_components:
                lines.append(f"- {comp}")
        else:
            lines.append("- None")

        lines.extend([
            "",
            f"Ethernet Card: {ethernet_card}",
            "",
            f"Server Purpose:\n{server_purpose}",
            "",
            f"Additional Requirement:\n{additional_requirement}",
        ])

        final_message = "\n".join(lines)

        # ============================
        # Save to DB
        # ============================
        try:
            with transaction.atomic():
                ContactMessageGlobal.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    subject="Build Your Own Server Request",
                    message=strip_tags(final_message),
                )
        except Exception as exc:
            messages.error(request, "Unable to save request.")
            return redirect("build_your_server")

        # ============================
        # Email
        # ============================
        try:
            send_mail(
                subject="BUILD YOUR OWN SERVER REQUEST",
                message=final_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["abhiraj@zacocomputer.com"],
                fail_silently=False,
            )
        except Exception as e:
            logger.error("Build Server email failed: %s", str(e))

        return redirect("thank_you")

    return render(request, "build_your_server.html")



def careers(request):
    return render(request, "main/careers.html")
