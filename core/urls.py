from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('apps.orders.urls')),
    path('reviews/', include('apps.reviews.urls')),
    path('shop/', include('apps.shop.urls')),
    path('users/', include('apps.users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)