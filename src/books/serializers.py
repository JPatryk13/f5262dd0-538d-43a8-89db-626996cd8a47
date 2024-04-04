from rest_framework import serializers

from .models import Book, Edition, Author


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ["publish_date", "publisher", "book", "language"]
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "birth_date", "death_date", "books"]
        depth = 1


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    editions = EditionSerializer(many=True)

    class Meta:
        model = Book
        fields = ["title", "first_published_year", "rating"]
        depth = 1
