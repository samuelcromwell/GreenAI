from django.contrib import admin
from django.urls import path
from website import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("products/", views.products, name="products"),
    path("products/<slug:slug>/", views.product_detail, name='product_detail'),
    path("solutions/", views.solutions, name="solutions"),
    path("solutions/<slug:slug>/", views.casestudy_detail, name="casestudies"),
    path("solutions/industry/<slug:slug>/", views.industry_detail, name="industry_detail"),
    path("sustainability/", views.sustainability, name="sustainability"),
    path("sustainability/<slug:slug>/", views.sustainability_detail, name='sustainability_detail'),
    path("sustainability/initiatives/<slug:slug>/", views.initiative_detail, name='initiative_detail'),
    path("support/", views.support, name="support"),
    path("partners/", views.partners, name="partners"),
    path("feedback/", views.feedback, name="feedback"),
    path("blogs/", views.blogs, name="blogs"),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path("footer/", views.footer_gallery_view, name="footer_gallery"),
    path("whitepapers/", views.whitepapers, name="whitepapers"),
    path("whitepapers/<slug:slug>/", views.whitepaper_detail, name='whitepaper_detail'),
    path("casestudies/", views.casestudies, name="casestudies"),
    path("FAQs/", views.FAQs, name='FAQs'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


