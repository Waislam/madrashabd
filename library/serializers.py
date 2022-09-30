from rest_framework import serializers
from accounts.serializers import MadrashaSerializer
from library.models import LibraryBook


class LibraryBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBook
        fields = ['id', 'madrasha', 'number', 'name', 'part', 'category', 'book_for_class',
                  'translator', 'publication', 'original_writer', 'language']
        depth = 3  # if you use depth you no need to use nested serializer to show dictionary of nested obj


class LibraryBookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBook
        fields = ['id', 'madrasha', 'name', 'part', 'category', 'book_for_class',
                  'translator', 'publication', 'original_writer', 'language']





