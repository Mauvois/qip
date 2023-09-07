from django.db import models

# Create your models here.


class user (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    # il faut hasher le password avec bcrypt, Argon2 ou scrypt
    password = models.CharField(max_length=200)
    picture = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)


class media (models.Model):
    created_time = models.DateTimeField()
    user = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )
    caption = models.CharField(max_length=50)
    media_type = models.CharField(max_length=50)
    permalink = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=50)
    storage_file = models.FileField(
        upload_to='your-upload-path/', storage='default_storage')
    is_published = models.BooleanField()
    category = models.IntegerField()


class post (models.Model):
    created_time = models.DateTimeField()
    user_id = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=1000)


class event (models.Model):
    created_time = models.DateTimeField()
    user_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    recurrence_id = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)


class contacter (models.Model):
    contacted_id = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )
    out_request_date = models.DateTimeField()
    in_request_date = models.DateTimeField()
    # set choices (pending, accepted, refused)
    invite_status = models.CharField(max_length=50)


class attendee (models.Model):
    event = models.ForeignKey(
        'event',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
    )
    # set choices (pending, accepted, refused)
    status = models.CharField(max_length=50)
