from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from alegrosz import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
            ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)