from rest_framework import viewsets

from .models import Book, Edition, Author
from .serializers import BookSerializer, EditionSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class EditionViewSet(viewsets.ModelViewSet):
    serializer_class = EditionSerializer
    queryset = Edition.objects.all()


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
