from django.contrib import admin
from .models import User, Media, Post, Event, Contacter, Attendee, Reference, Unique

admin.site.register(User)
admin.site.register(Media)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Contacter)
admin.site.register(Attendee)
admin.site.register(Reference)
admin.site.register(Unique)
