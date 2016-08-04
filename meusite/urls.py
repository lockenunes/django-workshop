from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^enquetes/', include('enquetes.urls')),
    url(r'^admin/', admin.site.urls),
]










