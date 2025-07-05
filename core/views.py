# core/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, Paragraph, WordIndex
from .serializers import RegisterSerializer, LoginSerializer, ParagraphSubmitSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import tokenize
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class ParagraphSubmitView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ParagraphSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']

        
        raw_paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        inserted_ids = []

        for content in raw_paragraphs:
            paragraph = Paragraph.objects.create(
                content=content,
                user=request.user
            )
            inserted_ids.append(str(paragraph.id))

            # Tokenize & map words to paragraph
            words = set(tokenize(content))  # use set to avoid duplicates
            WordIndex.objects.bulk_create([
                WordIndex(word=word, paragraph=paragraph) for word in words
            ], ignore_conflicts=True)  # ignores duplicates via unique_together

        return Response(
            {"message": f"{len(inserted_ids)} paragraph(s) added.", "paragraph_ids": inserted_ids},
            status=status.HTTP_201_CREATED
        )