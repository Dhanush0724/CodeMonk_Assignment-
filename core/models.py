# core/models.py

import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


# Custom user manager for handling user creation
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


# Custom User model
# Using AbstractBaseUser and PermissionsMixin to create a custom user model
class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email



## Paragraph model to store user-submitted paragraphs
# Each paragraph is linked to a user and contains the text content
class Paragraph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='paragraphs')
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Paragraph {self.id}'
    

# WordIndex model to map words to paragraphs
# This model allows efficient searching of paragraphs by words
class WordIndex(models.Model):
    word = models.CharField(max_length=100, db_index=True)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='word_mappings')

    class Meta:
        unique_together = ('word', 'paragraph')  

    def __str__(self):
        return f"{self.word} → {self.paragraph.id}"