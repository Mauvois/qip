from django.conf import settings
from rest_framework import viewsets
import requests
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwner, IsOwnerOrInvolved
# Note the changes here
from .models import User, Media, Post, Event, Contact, Attendee, Unique, RelationshipLabel, Tag, UserTag
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContactSerializer, AttendeeSerializer, UniqueSerializer, RelationshipLabelSerializer, TagSerializer, UserTagSerializer  # Note the changes here


class PermissionMixin(object):
    """
    Defines permission classes based on the action type.
    """

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class UserViewSet(PermissionMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MediaViewSet(PermissionMixin, ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class PostViewSet(PermissionMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EventViewSet(PermissionMixin, ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ContactViewSet(PermissionMixin, ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrInvolved]

class AttendeeViewSet(PermissionMixin, ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrInvolved]

class UniqueViewSet(PermissionMixin, ModelViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer

class RelationshipLabelViewSet(PermissionMixin, ModelViewSet):
    queryset = RelationshipLabel.objects.all()
    serializer_class = RelationshipLabelSerializer

class TagViewSet(PermissionMixin, ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserTagViewSet(PermissionMixin, ModelViewSet):
    queryset = UserTag.objects.all()
    serializer_class = UserTagSerializer

