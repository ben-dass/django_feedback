from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("reviews.urls")),
    path("profiles/", include("profiles.urls")),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
