from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('chat/', include('chat.urls')),
    path('character/', include('character.urls')),
    path('gallery/', include('gallery.urls')),
    path('account/', include('registration.urls', namespace="account")),
    path('news/', include('news.urls')),
    ] +static(settings.STATIC_URL , document_root=settings.STATIC_ROOT) +static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)

