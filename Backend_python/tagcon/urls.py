from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from . import settings

admin.site.site_header = 'TAGCON Admin'
admin.site.site_title = 'TAGCON Admin'
admin.site.index_title = 'For admins only'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',RedirectView.as_view(url='/api/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)