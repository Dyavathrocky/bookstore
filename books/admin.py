from django.contrib import admin
from .models import Book
# Register your models here.


#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","price")

admin.site.register(Book, BookAdmin)

#hi this is new space
