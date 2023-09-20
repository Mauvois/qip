from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import User, Media, Post, Event, Contacter, Attendee, Reference, Unique
from .serializers import UserSerializer, MediaSerializer, PostSerializer, EventSerializer, ContacterSerializer, AttendeeSerializer, ReferenceSerializer, UniqueSerializer


# @api_view(['GET'])
# def get_your_model(request):
#     your_models = YourModel.objects.all()
#     serializer = YourModelSerializer(your_models, many=True)
#     return Response(serializer.data)
# # Create your views here.


# def index(request):
#     return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class UniqueViewSet(viewsets.ModelViewSet):
    queryset = Unique.objects.all()
    serializer_class = UniqueSerializer
