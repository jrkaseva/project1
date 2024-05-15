from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('hblix/', include('hblix.urls')),
    path('admin/', admin.site.urls),
]