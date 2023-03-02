from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('faculty/', include('faculty.urls')),
    path('', RedirectView.as_view(url='registration/', permanent=True)),
    re_path(r'^select2/', include('django_select2.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
