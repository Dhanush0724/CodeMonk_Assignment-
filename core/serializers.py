# core/serializers.py

from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


# Serializers for user registration, login, paragraph submission, and word search
# These serializers handle the validation and serialization of user data
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'dob', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# Serializers for user login, paragraph submission, and word search
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

# Serializers for paragraph submission
# This serializer validates the text input and ensures it is not empty
class ParagraphSubmitSerializer(serializers.Serializer):
    text = serializers.CharField()

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Input text cannot be empty.")
        return value
    
# Serializer for word search functionality
# This serializer validates the word to be searched
class WordSearchSerializer(serializers.Serializer):
    word = serializers.CharField()

    def validate_word(self, value):
        word = value.strip().lower()
        if not word:
            raise serializers.ValidationError("Search word cannot be empty.")
        return word
