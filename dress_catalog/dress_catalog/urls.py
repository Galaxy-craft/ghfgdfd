from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dresses.views import dress_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dress_list, name='dress_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
