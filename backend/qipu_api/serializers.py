from rest_framework import serializers
from .models import User, Media, Post, Event, Contact, Attendee, Unique, RelationshipLabel, Tag, UserTag  # Note the changes here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contact
        fields = '__all__'

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class UniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unique
        fields = '__all__'

class RelationshipLabelSerializer(serializers.ModelSerializer):  
    class Meta:
        model = RelationshipLabel
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Tag
        fields = '__all__'

class UserTagSerializer(serializers.ModelSerializer):  
    class Meta:
        model = UserTag
        fields = '__all__'
