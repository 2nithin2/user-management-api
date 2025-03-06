"""
This module defines URL patterns for the User API.
Each URL is mapped to a corresponding view function in views.py.
"""

# Import necessary modules for URL configuration
from django.urls import path  # Django's built-in path function for URL routing

# Import view functions that handle API requests
from .views import get_users, create_user, user_detail

# Define URL patterns for user-related API endpoints
urlpatterns = [
    path('users/', get_users, name='get_users'),  
    # Endpoint to retrieve all users (GET request)

    path('users/create/', create_user, name='create_user'),  
    # Endpoint to create a new user (POST request)

    path('users/<int:pk>', user_detail, name='user_detail')  
    # Endpoint to retrieve, update, or delete a specific user by ID (GET, PUT, DELETE)
]
