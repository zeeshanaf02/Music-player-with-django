from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('player.urls')),  # This includes your 'player' app's URL patterns
]

# Append static and media URL patterns without overwriting urlpatterns
urlpatterns += staticfiles_urlpatterns()  # Serves static files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serves media files during development
