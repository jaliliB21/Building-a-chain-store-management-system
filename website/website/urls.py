from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('users.urls')),
    path('', include('main.urls')),
    path('', include('news.urls')),
    path('', include('stores.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
