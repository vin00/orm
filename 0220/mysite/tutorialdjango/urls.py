from django.contrib import admin
from django.urls import path
from main.views import index, a, b, c

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('a/', a),
    path('b/', b),
    path('c/', c),
]
