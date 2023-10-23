import os
from datetime import datetime, timedelta

from django.http import JsonResponse
from django.conf import settings
from rest_framework import viewsets
from oauth2_provider.decorators import protected_resource
from oauth2_provider.views import TokenView
from oauth2_provider.models import AccessToken, Application
import requests
from requests.exceptions import RequestException
from django.shortcuts import render
from oauth2_provider.views import AuthorizationView

from .models import User, Media, Post, Event, Contacter, Attendee, Unique
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContacterSerializer, AttendeeSerializer, UniqueSerializer


class ProtectedResourceViewSet(viewsets.ModelViewSet):
    @protected_resource()
    def dispatch(self, *args, **kwargs):
        return super(ProtectedResourceViewSet, self).dispatch(*args, **kwargs)


class UserViewSet(ProtectedResourceViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MediaViewSet(ProtectedResourceViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class PostViewSet(ProtectedResourceViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EventViewSet(ProtectedResourceViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContacterViewSet(ProtectedResourceViewSet):
    queryset = Contacter.objects.all()
    serializer_class = ContacterSerializer


class AttendeeViewSet(ProtectedResourceViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer


class UniqueViewSet(ProtectedResourceViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer



def oauth_callback(request):
    code = request.GET.get('code')

    try:
        # Exchange the code for an access token (modify with your OAuth server details)
        response = requests.post(settings.OAUTH_SERVER_URL, data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:8000/callback/',
            'client_id': os.environ['ID'],
            'client_secret': os.environ['SECRET']
        })

        data = response.json()

        expires_at = datetime.now() + timedelta(seconds=data['expires_in'])

        # Assuming you have user info, link the user too
        user_instance = request.user  # If the current user is the user related to the token

        # Fetch the related application instance based on the client_id
        # This assumes that you have only one application or the 'client_id' is unique to an application
        application_instance = Application.objects.get(
            client_id=os.environ['ID'])

        access_token = AccessToken(
            token=data['access_token'],
            expires=expires_at,
            token_type=data['token_type'],
            user=user_instance,
            application=application_instance,
            scope=data.get('scope', '')
        )
        access_token.save()

        return JsonResponse({'token': data['access_token'], 'expires_at': expires_at.strftime('%Y-%m-%dT%H:%M:%S')}, status=201)

    except Application.DoesNotExist:
        return JsonResponse({"error": "Application not found."}, status=400)
    except RequestException as e:
        # Handle request exceptions here
        return JsonResponse({"error": "Failed to connect to OAuth server.", "details": str(e)}, status=500)
