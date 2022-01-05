from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Add a custom validation error
        if not email:
            raise ValueError('User must have an email address') 
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # Use the set_password method to hash the password
        user.set_password(password)
        # Call save to save the user to the database
        user.save()
        # Always return the user!
        return user

    def create_superuser(self, email, password):
        # Use the custom create_user method above to create
        # the user.
        user = self.create_user(email, password)
        # Add the required is_superuser and is_staff properties
        # which must be set to True for superusers
        user.is_superuser = True
        user.is_staff = True
        # Save the user to the database with the new properties
        user.save()
        # Always return the user!
        return user

# Inherit from AbstractBaseUser and PermissionsMixin:
class User(AbstractBaseUser, PermissionsMixin):
    # As with any Django models, we need to define the fields
    # for the model with the type and options:
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Tell Django to use the email field as the unique identifier for the
    # user account instead of its built in behavior of using the username.
    USERNAME_FIELD = ('email')
    objects = UserManager()
    def __str__(self):
        """Return string representation of the user"""
        return self.email