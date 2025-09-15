
from django.urls import path

from globalwebsite import views

urlpatterns = [    
    path('',views.home,name="home"),
    path('about-us/',views.about_us,name="about_us"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),
    path('contact-us/',views.contact,name="contact"),
    path('itad-services/',views.itadservices,name="itad-services"),
    path('it-hardware/',views.it_hardware,name="it-hardware"),
    path('server-maintenance/',views.server_maintenance,name="server-maintenance"),
    path('storage-maintenance/',views.storage_maintenance,name="storage-maintenance"),
    path('network-maintenance/',views.network_maintenance,name="network-maintenance"),
    path('rental-services/',views.rental_services,name="rental-services"),
    path('infrastructure-managed-service/',views.infrastructure_service,name="infrastructure-managed-service"),
    path('global-it/',views.global_it,name="global-it"),
    path('microsoft-vm/',views.microsoft_vm,name="microsoft-vm"),
    path('privacy-policy/',views.privacy,name="privacy"),
    path('terms-and-conditions/',views.term,name="term"),
    # path('shop',views.shop,name="shop"),
    # path('add/', views.add_product, name='add_product'),
    path('add-product/', views.manage_products, name='add_or_edit_product'),
    path('shop/', views.shop, name='shop'),
    # path('shop/<slug:category_slug>/', views.shop, name='shop_by_category'),
    path('shop/category/<slug:category_slug>/', views.shop, name='shop_by_category'),

    # path('shop/<slug:category_slug>/<slug:subcategory_slug>/', views.shop, name='shop_by_subcategory'),

    # path('category/<slug:category_slug>/', views.shop, name='product_by_category'),

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/update_all/', views.cart_update_all, name='cart_update_all'),


    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # path('uk',views.uk_home,name="uk-home"),
    # path('uae',views.uae_home,name="uae-home"),
    # path('ca',views.canada_home,name="canada-home"),
    # path('in',views.india_home,name="india-home"),

    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<int:order_id>/', views.order_success,
         name='order_success'),
         
    path("blog/create/", views.create_blog, name="create_blog"),

    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.blogs_by_category, name='blogs_by_category'),
    path('subcategory/<slug:slug>/', views.blogs_by_subcategory, name='blogs_by_subcategory'),

    path('tag/<slug:slug>/', views.blogs_by_tag, name='blogs_by_tag'),
    path('archive/<int:year>/<int:month>/', views.blogs_by_archive, name='blogs_by_archive'),

    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),

    path('thank-you/', views.thank_you, name='thank_you'),






# urls.py

    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/', views.shop, name='shop_by_category'),
    path('shop/<slug:category_slug>/<slug:subcategory_slug>/', views.shop, name='shop_by_subcategory'),

]

