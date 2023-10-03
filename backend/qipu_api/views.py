from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import User, Media, Post, Event, Contacter, Attendee, Reference, Unique
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContacterSerializer, AttendeeSerializer, ReferenceSerializer, UniqueSerializer
from oauth2_provider.decorators import protected_resource


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class ContacterViewSet(viewsets.ModelViewSet):
    queryset = Contacter.objects.all()
    serializer_class = ContacterSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)


class UniqueViewSet(viewsets.ModelViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer

    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(UserViewSet, self).dispatch(*args, **kwargs)
