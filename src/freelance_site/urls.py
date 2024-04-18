from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from freelance_site.views import about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('', include('order.urls', namespace='order')),
    path('account/', include('account.urls')),
    path('api/', include('api.urls')),
    path('account/', include('django.contrib.auth.urls')),
]

handler404 = 'freelance_site.views.page_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
