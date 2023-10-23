import os
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
import requests
from requests.exceptions import RequestException
from django.shortcuts import render
from .models import User, Media, Post, Event, Contacter, Attendee, Unique
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContacterSerializer, AttendeeSerializer, UniqueSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContacterViewSet(viewsets.ModelViewSet):
    queryset = Contacter.objects.all()
    serializer_class = ContacterSerializer


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer


class UniqueViewSet(viewsets.ModelViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer
