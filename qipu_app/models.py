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
    user_id = models.CharField(max_length=50)
    recurrence_id = models.ForeignKey('self'null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField(max_length=50)
    media_type = models.CharField(max_length=50)
    permalink = models.CharField(max_length=50)
    shortcode = models.CharField(max_length=50)
    storage_file = models.FileField(
        upload_to='your-upload-path/', storage=default_storage)
    is_published = models.BooleanField()
    category = models.IntegerField()


class post (models.Model):
    user_id = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_time = models.DateTimeField()
        
    privacy_settings = 
