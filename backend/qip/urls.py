from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('qipu_api.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, view=serve)
