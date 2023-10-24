from rest_framework import permissions
from .models import User, Contact, Attendee, Media, Post, Event, RelationshipLabel, UserTag

class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # For models with a 'user' attribute
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # For the User model itself
        if isinstance(obj, User):
            return obj == request.user

        # For the Contact model
        if isinstance(obj, Contact):
            return obj.requester == request.user or obj.recipient == request.user
        
        # Additional Models
        if isinstance(obj, (Media, Post, Event, RelationshipLabel, UserTag)):
            return obj.user == request.user
        
        return False

class IsOwnerOrInvolved(permissions.BasePermission):
    """
    Custom permission for Attendee and Contact. 
    Ensures that both the creator and the invited/contacted user can see the object.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is either the event creator or the attendee
        if isinstance(obj, Attendee):
            return obj.event.user == request.user or obj.user == request.user
        
        # Check if the requesting user is either the requester or the recipient
        if isinstance(obj, Contact):
            return obj.requester == request.user or obj.recipient == request.user
        
        return False
