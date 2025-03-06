"""
This module defines a serializer for the User model using Django REST Framework (DRF).
A serializer converts complex Django model instances into JSON format and vice versa.
"""

from rest_framework import serializers  # Importing Django REST Framework's serializers module
from .models import User  # Importing the User model from the current app's models

class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer is a ModelSerializer that converts User model instances 
    into JSON format and validates incoming JSON data.
    """

    class Meta:
        """
        Meta class provides metadata to the serializer.
        - model: Specifies the Django model associated with the serializer.
        - fields: '__all__' means all fields of the User model will be serialized.
        """
        model = User  
        fields = '__all__'  # Includes all fields from the User model in the API response
