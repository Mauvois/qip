import os
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
import requests
from requests.exceptions import RequestException
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsOwner
from .models import User, Media, Post, Event, Contacter, Attendee, Unique
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContacterSerializer, AttendeeSerializer, UniqueSerializer


class BaseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]


class PermissionMixin(object):
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MediaViewSet(PermissionMixin, BaseViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class PostViewSet(PermissionMixin, BaseViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EventViewSet(BaseViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContacterViewSet(BaseViewSet):
    queryset = Contacter.objects.all()
    serializer_class = ContacterSerializer


class AttendeeViewSet(BaseViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer


class UniqueViewSet(BaseViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer
