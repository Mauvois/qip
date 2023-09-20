from django.db import models
from .utility import media_file_upload
from datetime import datetime, timedelta

future_date = models.DateTimeField(default=datetime.now() + timedelta(days=30))


def validate_bio_length(value):
    if len(value) < 5:  # Assuming you want a minimum of 10 characters
        raise ValidationError('Bio must be at least 10 characters long.')

# Create your models here.


class Unique(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)

    # Vous pouvez ajouter d'autres champs au besoin.


class User (models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    # il faut hasher le password avec bcrypt, Argon2 ou scrypt
    password = models.CharField(max_length=1000, blank=False)
    picture = models.CharField(
        max_length=500, default='default_profile_picture.jpg')
    bio = models.CharField(max_length=250, validators=[
                           validate_bio_length], default='New user at QipU!')


class Media (models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False
    )
    caption = models.CharField(max_length=150)
    media_type = models.CharField(max_length=20, blank=False)
    permalink = models.CharField(max_length=500, blank=False)
    shortcode = models.CharField(max_length=50)
    storage_file = models.FileField(upload_to=media_file_upload, blank=False)
    is_published = models.BooleanField(default=False)
    category = models.IntegerField()


class Post (models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, blank=False
    )
    content = models.TextField(max_length=1000, blank=False)


class Event (models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    location = models.CharField(max_length=150, blank=False)
    start_time = models.DateTimeField(blank=False)
    end_time = models.DateTimeField()
    recurrence_id = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)


class Contacter (models.Model):
    contacted_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE, blank=False
    )
    out_request_date = models.DateTimeField(blank=False)
    in_request_date = models.DateTimeField(blank=False)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    )
    invite_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, blank=False, default='pending')


class Attendee (models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE, blank=False
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, blank=False
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    )
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, blank=False, default='pending')


class Reference(models.Model):
    # Champs de clé étrangère pour référencer les autres tables
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    media = models.ForeignKey(
        Media, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    contact = models.ForeignKey(
        Contacter, on_delete=models.CASCADE, null=True, blank=True)
    attendee = models.ForeignKey(
        Attendee, on_delete=models.CASCADE, null=True, blank=True)
