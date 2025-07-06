# core/urls.py

from django.urls import path
from .views import RegisterView, LoginView, ParagraphSubmitView, WordSearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('paragraphs/', ParagraphSubmitView.as_view(), name='submit-paragraphs'),
    path('search/', WordSearchView.as_view(), name='search-word'),
]
