from rest_framework import serializers
from .models import User, Media, Post, Event, Contact, Attendee, Unique, RelationshipLabel, Tag, UserTag  # Note the changes here

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'created_time', 'picture', 'bio']
        
    def create(self, validated_data):
        # Remove the password from the validated data and create a user
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

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
