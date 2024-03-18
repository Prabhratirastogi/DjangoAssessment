from .models import Book, Person
from rest_framework import serializers
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'birth_year', 'death_year')

class BookSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    authors = PersonSerializer(many=True)
    translators = PersonSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'authors',
            'translators',
            'subjects',
            'bookshelves',
            'languages',
            'copyright',
            'media_type',
            'formats',
            'download_count'
        )

    def get_id(self, book):
        return book.gutenberg_id

    def get_bookshelves(self, book):
        return list(book.bookshelves.values_list('name', flat=True).order_by('name'))

    def get_formats(self, book):
        return {f.mime_type: f.url for f in book.format_set.all()}

    def get_languages(self, book):
        return list(book.languages.values_list('code', flat=True).order_by('code'))

    def get_subjects(self, book):
        return list(book.subjects.values_list('name', flat=True).order_by('name'))
