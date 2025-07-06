# core/urls.py

from django.urls import path
from .views import RegisterView, LoginView, ParagraphSubmitView, WordSearchView

# URL patterns for the core app
# These patterns map URLs to their respective views for user registration, login, paragraph submission, and word search
# Each view handles the request and response for the corresponding functionality
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('paragraphs/', ParagraphSubmitView.as_view(), name='submit-paragraphs'),
    path('search/', WordSearchView.as_view(), name='search-word'),
]
