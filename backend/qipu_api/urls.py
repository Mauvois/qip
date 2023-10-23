from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet, MediaViewSet, PostViewSet, EventViewSet, ContacterViewSet, AttendeeViewSet, UniqueViewSet, oauth_callback


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'media', MediaViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'contacters', ContacterViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'uniques', UniqueViewSet)


urlpatterns = [
    path('callback/', oauth_callback, name='oauth-callback'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]
