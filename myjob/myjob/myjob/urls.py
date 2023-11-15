from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_job.urls')),
]


if settings.DEBUG:
    if __name__ == '__main__':
        urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA.ROOT)
