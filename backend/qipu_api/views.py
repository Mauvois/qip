from django.conf import settings
from rest_framework import viewsets
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
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


class SignupView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if User.objects.filter(username=username).exists():
            raise ValidationError({'error': 'Username already exists'})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)

        # You can add more fields if needed

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]  # Allow any user to login

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError({'error': 'Invalid Credentials'})

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({'token': token, 'user': UserSerializer(user).data}, status=status.HTTP_200_OK)


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
