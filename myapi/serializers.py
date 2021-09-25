from rest_framework import serializers
from .models import Author
from .models import Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'created_date', 'added_by_id')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'created_date', 'added_by_id', 'author_id')


