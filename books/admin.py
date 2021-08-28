from django.contrib import admin
from .models import Author, Book
# Register your models here.

class BookInlineAdmin(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInlineAdmin
    ]

admin.site.register(Author, AuthorAdmin)