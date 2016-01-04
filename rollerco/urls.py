from django.conf.urls import include, url
from django.contrib import admin
from rollerco import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^', include('mainApp.urls')),
]
