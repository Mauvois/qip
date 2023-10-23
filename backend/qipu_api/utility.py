import os
import uuid
from rest_framework_jwt.utils import jwt_payload_handler

# code proposé par ChatGPT3.5 tel quel


def media_file_upload(instance, filename):
    # Generate a unique filename using UUID
    filename_base, filename_ext = os.path.splitext(filename)
    unique_filename = f"{uuid.uuid4().hex}{filename_ext}"
    # Determine the directory structure
    return f"media_files/{instance.user.username}/{unique_filename}"


def validate_bio_length(value):
    if len(value) < 5:
        raise ValidationError('Bio must be at least 10 characters long.')
    
def custom_jwt_payload_handler(user):
    payload = jwt_payload_handler(user)
    # Add custom claims here, e.g.:
    # payload['custom_claim'] = 'custom_value'
    return payload