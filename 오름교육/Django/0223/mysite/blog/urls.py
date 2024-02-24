from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("test/", views.blog_test, name="test"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]