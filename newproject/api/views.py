"""
This module defines API views for managing User model data using Django REST Framework (DRF).
It includes endpoints to retrieve, create, update, and delete users.
"""

# Import necessary Django REST Framework components
from rest_framework.decorators import api_view  # Allows function-based API views
from rest_framework.response import Response  # Standardized API response format
from rest_framework import status  # HTTP status codes for responses

# Import the User model and its serializer
from .models import User
from .serialzer import UserSerializer

@api_view(['GET'])
def get_users(request):
    """
    Retrieve all users from the database and return them as JSON.

    - Method: GET
    - URL: /users/
    - Response: List of all users
    """
    users = User.objects.all()  # Fetch all users from the database
    serializer = UserSerializer(users, many=True)  # Serialize multiple user objects
    return Response(serializer.data)  # Return serialized data in JSON format

@api_view(['POST'])
def create_user(request):
    """
    Create a new user in the database.

    - Method: POST
    - URL: /users/create/
    - Request Body: JSON data containing user details (e.g., {"name": "Alice", "age": 25})
    - Response: Newly created user data or validation errors
    """
    serializer = UserSerializer(data=request.data)  # Deserialize incoming JSON data
    if serializer.is_valid():  # Validate the input data
        serializer.save()  # Save new user to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created user data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update, or delete a specific user by their primary key (ID).

    - Methods:
        - GET: Retrieve user details
        - PUT: Update user details
        - DELETE: Remove the user from the database
    - URL: /users/<pk>/
    - Response: JSON data of the user (for GET/PUT) or a success status (for DELETE)
    """
    try:
        user = User.objects.get(pk=pk)  # Fetch user by primary key (ID)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if user does not exist

    if request.method == 'GET':
        """
        Retrieve user details.
        """
        serializer = UserSerializer(user)  # Serialize user object
        return Response(serializer.data)  # Return user data

    elif request.method == 'PUT':
        """
        Update user details.
        """
        serializer = UserSerializer(user, data=request.data)  # Deserialize and validate incoming data
        if serializer.is_valid():
            serializer.save()  # Save updated user data
            return Response(serializer.data)  # Return updated user details
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    elif request.method == 'DELETE':
        """
        Delete a user from the database.
        """
        user.delete()  # Remove user from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return success status
