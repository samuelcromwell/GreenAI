from django.contrib import admin
from django.urls import path, include
from website import views


urlpatterns = [
    path("", views.index, name="home"),
    # path("about", views.about, name="about"),
    # path("blog", views.blog, name="blog"),
    # path("services", views.services, name="services"),
    # path("contact", views.contact, name="contact"),
    # path("single-blog", views.singleblog, name="singleblog"),
]