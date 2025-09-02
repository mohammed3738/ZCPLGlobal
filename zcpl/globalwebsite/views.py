from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .cart import Cart
from .forms import *
from django.db.models import Q, Avg
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm
# from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings
# Create your views here.

from django.db.models import Count
from django.utils.timezone import now


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
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # ✅ Validate including captcha
            name = request.POST.get('username')
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
            success = True  # success only after valid submission
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form, 'success': success})






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

        # Multiple category selection
        category_ids = request.POST.getlist('categories')
        selected_subcategories = SubCategory.objects.filter(id__in=category_ids)

        if not all([name, price]) or not selected_subcategories:
            error = "Name, Price, and at least one Category are required."
        else:
            if not editing:
                # Create product
                product = Product.objects.create(
                    name=name,
                    price=price,
                    available=available,
                    short_description=short_description,
                    description=description,
                )
                product.categories.set(selected_subcategories)
                if image:
                    product.image = image
                    product.save()
            else:
                # Update product
                product = product_to_edit
                product.name = name
                product.price = price
                product.available = available
                product.short_description = short_description
                product.description = description
                if image:
                    product.image = image
                product.save()
                product.categories.set(selected_subcategories)

            # Handle multiple gallery images
            gallery_images = request.FILES.getlist('gallery_images')
            for g_image in gallery_images:
                ProductImage.objects.create(product=product, image=g_image)

            return redirect('add_or_edit_product')

    # Fetch all subcategories
    subcategories = SubCategory.objects.all()

    # Search & sort
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

    return render(request, 'main/shop.html', {
        'category': category,
        'subcategory': subcategory,
        'products': page_obj,
        'categories': Category.objects.all(),
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



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    reviews = product.reviews.all().order_by('-created_at')
    cart_product_form = CartAddProductForm()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')

        if name and comment and rating:
            Review.objects.create(
                product=product,
                name=name,
                comment=comment,
                rating=int(rating)
            )
            return redirect('product_detail', slug=product.slug)

    return render(request, 'main/product_detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'reviews': reviews,
        'review_count': reviews.count()

    })





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
    sub_categories = SubCategoryBlog.objects.annotate(num_posts=Count('blog'))
    tags = Tag.objects.all()
    archives = Blog.objects.dates('created_at', 'month', order='DESC')

    context = {
        'blogs': blogs,
        'categories': categories,
        'tags': tags,
        'archives': archives,
    }
    return render(request, 'blog/blog_list.html', context)

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save_m2m()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})

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


def blogs_by_category(request, slug):
    category = get_object_or_404(CategoryBlog, slug=slug)
    blogs = Blog.objects.filter(category=category)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'selected_category': category})

def blogs_by_subcategory(request, slug):
    subcategory = get_object_or_404(SubCategoryBlog, slug=slug)
    blogs = Blog.objects.filter(sub_category=subcategory)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'selected_subcategory': subcategory})


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
        "categories": categories,
        "tags": tags,
        "archives": archives,
    })



def sitemap(request):
    return render(request,'sitemap.xml', content_type="application/xml")

def robots_txt(request):
    return render(request,'robots.txt', content_type="text/plain")


