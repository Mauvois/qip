from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, MediaViewSet, PostViewSet, EventViewSet,
    ContactViewSet, AttendeeViewSet, UniqueViewSet,
    RelationshipLabelViewSet, TagViewSet, UserTagViewSet
)

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'media', MediaViewSet)
router.register(r'posts', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'attendees', AttendeeViewSet)
router.register(r'uniques', UniqueViewSet)
router.register(r'relationship_labels', RelationshipLabelViewSet)
router.register(r'tags', TagViewSet)
router.register(r'user_tags', UserTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
