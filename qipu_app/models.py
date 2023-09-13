from django.db import models
from qipu_app.utility import media_file_upload

# Create your models here.


class Unique(models.Model):
    created_time = models.DateTimeField()

    # Vous pouvez ajouter d'autres champs au besoin.


class User (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    # il faut hasher le password avec bcrypt, Argon2 ou scrypt
    password = models.CharField(max_length=200)
    picture = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)


class Media (models.Model):
    created_time = models.DateTimeField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    caption = models.CharField(max_length=50)
    media_type = models.CharField(max_length=50)
    permalink = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=50)
    storage_file = models.FileField(upload_to=media_file_upload)
    is_published = models.BooleanField()
    category = models.IntegerField()


class Post (models.Model):
    created_time = models.DateTimeField()
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=1000)


class Event (models.Model):
    created_time = models.DateTimeField()
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    recurrence_id = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)


class Contacter (models.Model):
    contacted_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    out_request_date = models.DateTimeField()
    in_request_date = models.DateTimeField()
    INVITE_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    )
    invite_status = models.CharField(max_length=50)


class Attendee (models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    # set choices (pending, accepted, refused)
    status = models.CharField(max_length=50)


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
