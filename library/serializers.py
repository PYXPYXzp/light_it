from rest_framework import serializers
from library.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'book_set',
        )


class BooksSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'user_now',
            'user_before',
            'date',
        )
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True, read_only=True, source='book_set')

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'books',
        )
