from django.contrib import admin
from django.urls import path
from main.views import (
    index,
    about,
    contact,
    notice,
    notice1,
    notice2,
    notice3,
    abcd,
    vin,
    mini,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(''. index),
    path('about/', about),
    path('notice/', notice),
    path('notice/1', notice1),
    path('notice/2', notice2),
    path('notice/3', notice3),
    path('contact/', contact),
    path('a/b/c/d', abcd),
    path('user/vin', vin),
    path('user/mini', mini),
]