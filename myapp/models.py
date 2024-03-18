from django.db import models

class Book(models.Model):
    authors = models.ManyToManyField('Person')
    bookshelves = models.ManyToManyField('Bookshelf')
    copyright = models.BooleanField(null=True)
    download_count = models.PositiveIntegerField(blank=True, null=True)
    gutenberg_id = models.PositiveIntegerField(unique=True, null=True)
    languages = models.ManyToManyField('Language')
    media_type = models.CharField(max_length=16, null=True)
    subjects = models.ManyToManyField('Subject')
    title = models.CharField(blank=True, max_length=1024, null=True)
    translators = models.ManyToManyField(
        'Person', related_name='books_translated')
    genre = models.CharField(max_length=64, blank=True, null=True)  # Added field for genre

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)

class Bookshelf(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.code

class Person(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
