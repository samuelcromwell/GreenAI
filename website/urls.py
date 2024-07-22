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
    path("solutions/", views.solutions, name="solutions"),
    path("sustainability/", views.sustainability, name="sustainability"),
    path("support/", views.support, name="support"),
    path("partners/", views.partners, name="partners"),
    path("feedback/", views.feedback, name="feedback"),
    # path("blog", views.blog, name="blog"),
    # path("services", views.services, name="services"),
    # path("single-blog", views.singleblog, name="singleblog"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
