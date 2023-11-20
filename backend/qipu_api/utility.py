import os
import uuid
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

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


def set_token_cookie(response: HttpResponse, token: str) -> None:
    """Sets the JWT token as a httpOnly cookie."""
    response.set_cookie(
        key='authToken',
        value=token,
        httponly=True,
        samesite='None',  # Setting the SameSite attribute to 'None'
        secure=True,      # Ensuring the cookie is sent over HTTPS
        # Add other properties as needed
    )


class TokenFromCookieMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract token from cookie
        token = request.COOKIES.get('authToken', None)

        # Print all the cookies present
        print("Cookies present:", request.COOKIES)

        # If token is found, print it and set it in the Authorization header
        if token:
            print("Token extracted:", token)
            request.META['HTTP_AUTHORIZATION'] = f"Bearer {token}"
            print("Authorization header set:",
                  request.META['HTTP_AUTHORIZATION'])

        response = self.get_response(request)
        print(response)
        return response


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            if request.path in [reverse('login'), reverse('signup')]:
                return redirect('Dashboard')
        return None
