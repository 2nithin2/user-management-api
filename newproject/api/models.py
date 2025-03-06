from django.db import models  

class User(models.Model):  
    """Model representing a user with a name and optional age field."""
    
    name = models.CharField(max_length=100)  # Stores the user's name (max 100 characters).
    age = models.IntegerField(null=True)  # Stores the user's age (nullable).

    def __str__(self):
        """Returns the string representation of the user (name)."""
        return self.name  
