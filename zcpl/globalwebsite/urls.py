
from django.urls import path

from globalwebsite import views

from django.contrib.sitemaps.views import sitemap
from india.sitemaps import IndiaStaticSitemap
from uae.sitemaps import UAESitemap
from uk.sitemaps import UKSitemap
from globalwebsite.sitemaps import *
from casestudies.sitemaps import CaseStudyListSitemap, CaseStudyDetailSitemap

sitemaps = {
    "india": IndiaStaticSitemap,
    "uae": UAESitemap,
    "uk": UKSitemap,
    "products": ProductSitemap,
    "case_studies": CaseStudyDetailSitemap,
    "categories": CategorySitemap,
    "subcategories": SubCategorySitemap,

}


urlpatterns = [    
    path('',views.home,name="home"),
    path('about-us/',views.about_us,name="about_us"),
    path('services/',views.services,name="services"),
    path('contact/',views.contact,name="contact"),
    path('contact-us/',views.contact,name="contact"),
    path('itad-services/',views.itadservices,name="itad-services"),
    path('it-hardware/',views.it_hardware,name="it-hardware"), 
    path('vmware-third-party-support/',views.vmware_support,name="vmware-support"),
    path('microsoft-thirdparty-support/',views.microsoft_support,name="microsoft-thirdparty-support"),
    path('server-maintenance/',views.server_maintenance,name="server-maintenance"),
    path('storage-maintenance/',views.storage_maintenance,name="storage-maintenance"),
    path('network-maintenance/',views.network_maintenance,name="network-maintenance"),
    path('rental-services/',views.rental_services,name="rental-services"),
    path('infrastructure-managed-service/',views.infrastructure_service,name="infrastructure-managed-service"),
    path('global-it/',views.global_it,name="global-it"),
    path('microsoft-vm/',views.microsoft_vm,name="microsoft-vm"),
    path('email-migration-services/',views.email_migration,name="email-migration"),
    path('privacy-policy/',views.privacy,name="privacy"),
    path('terms-and-conditions/',views.term,name="term"),
    # path('shop',views.shop,name="shop"),
    # path('add/', views.add_product, name='add_product'),
    path('add-product/', views.manage_products, name='add_or_edit_product'),
    # path('shop/', views.shop, name='shop'),
    # path('shop/<slug:category_slug>/', views.shop, name='shop_by_category'),
    # path('shop/category/<slug:category_slug>/', views.shop, name='shop_by_category'),

    # path('shop/<slug:category_slug>/<slug:subcategory_slug>/', views.shop, name='shop_by_subcategory'),

    # path('category/<slug:category_slug>/', views.shop, name='product_by_category'),

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/update_all/', views.cart_update_all, name='cart_update_all'),
    

    path('ppc/products/', views.ppc_product_manage, name='ppc-product-manage'),
    path('ppc/products/edit/<int:pk>/', views.ppc_product_manage, name='ppc-product-edit'),
    path('ppc/products/delete/<int:pk>/', views.ppc_product_delete, name='ppc-product-delete'),
    # PPC Category landing pages
    path('ppc/category/<slug:slug>/', views.ppc_category_detail, name='ppc_category_detail'),

    # PPC Subcategory pages
    path('ppc/subcategory/<slug:slug>/', views.ppc_subcategory_detail, name='ppc_subcategory_detail'),
    path(
        'ppc/<slug:slug>/',
        views.ppc_product_detail,
        name='ppc_product_detail'
    ),
    path('quote/submit/', views.ppc_quote_submit, name='ppc_quote_submit'),

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
    # path("add/", views.add_blog, name="add_blog"),

    path("blog/add/", views.add_blog, name="add_blog"),
    path("blog/<int:blog_id>/edit/", views.edit_blog, name="edit_blog"),

    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:slug>/', views.blogs_by_category, name='blogs_by_category'),
    # path('subcategory/<slug:slug>/', views.blogs_by_subcategory, name='blogs_by_subcategory'),

    path('tag/<slug:slug>/', views.blogs_by_tag, name='blogs_by_tag'),
    path('archive/<int:year>/<int:month>/', views.blogs_by_archive, name='blogs_by_archive'),

    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', views.logout_view, name='logout'),

    path('thank-you/', views.thank_you, name='thank_you'),



    path("gmc.xml", views.google_xml_feed, name="google_xml_feed"),

    path("search-ajax/", views.ajax_product_search, name="ajax_product_search"),


# urls.py

    path('shop/', views.shop, name='shop'),
    path('shop/<slug:category_slug>/', views.shop, name='shop_by_category'),
    path('shop/<slug:category_slug>/<slug:subcategory_slug>/', views.shop, name='shop_by_subcategory'),
    
    path('categories/', views.category_manager, name='category_manager'),
    path('categories/edit/<int:category_id>/', views.category_manager, name='edit_category'),

    path('subcategories/', views.subcategory_manager, name='subcategory_manager'),
    path('subcategories/edit/<int:subcategory_id>/', views.subcategory_manager, name='edit_subcategory'),

    path('api/request-quote/', views.request_quote_api, name='request_quote_api'),
    path(
        "sitemap-main.xml",
        sitemap,
        {"sitemaps": {"main": StaticViewSitemap,"sub-category": SubCategorySitemap,'categorys': CategorySitemap,}}),

    path("sitemap.xml", views.sitemap_index, name="sitemap_index"),
    path("sitemap-india.xml", sitemap, {"sitemaps": {"india": IndiaStaticSitemap}}),
    path("sitemap-uae.xml", sitemap, {"sitemaps": {"uae": UAESitemap}}),
    path("sitemap-uk.xml", sitemap, {"sitemaps": {"uk": UKSitemap}}),
    path("sitemap-products.xml", sitemap, {"sitemaps": {"products": ProductSitemap}}),
    path("sitemap-case-studies.xml",sitemap,{"sitemaps": {"case_list": CaseStudyListSitemap,"case_detail": CaseStudyDetailSitemap,}}),
    path("sitemap-blogs.xml", sitemap, {"sitemaps": {"blogs": BlogSitemap}}),


    path(
        'build-your-server/',
        views.build_your_server,
        name='build_your_server'
    ),
    # path("careers/", views.careers, name="careers"),
    path("api/server-models/", views.get_server_models, name="get_server_models"),

    # path("sitemap-products.xml",sitemap,{"sitemaps": {"products": ProductSitemap,"categories": CategorySitemap,"subcategories": SubCategorySitemap,}}),
    path("newsletter/subscribe/", views.newsletter_subscribe, name="newsletter_subscribe"),

]

