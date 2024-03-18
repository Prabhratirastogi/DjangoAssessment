from django.contrib import admin
from .models import Book, Bookshelf, Language, Person, Subject

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Bookshelf)
class BookshelfAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
