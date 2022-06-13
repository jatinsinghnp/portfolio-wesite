from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    PortfolioPageView,
    ContactUsView,
    BlogPageView,
    BlogPostView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("about/", AboutPageView.as_view(), name="about-page"),
    path("portfolio/", PortfolioPageView.as_view(), name="port-page"),
    path("contact_us/", ContactUsView.as_view(), name="contact-page"),
    path("blog/", BlogPageView.as_view(), name="blog-page"),
    path("blogpost/<slug:slug>", BlogPostView.as_view(), name="blog-post-page"),
]
