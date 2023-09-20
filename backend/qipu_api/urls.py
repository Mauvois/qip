# mainapp/urls.py
from django.urls import path, include
# from qipu_api import views
# from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
# from rest_framework import routers, serializers, viewsets
from .views import UserViewSet, MediaViewSet, PostViewSet, EventViewSet, ContacterViewSet, AttendeeViewSet, ReferenceViewSet, UniqueViewSet



# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'media', MediaViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'contacters', ContacterViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'references', ReferenceViewSet)
router.register(r'uniques', UniqueViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
