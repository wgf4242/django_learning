from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
	fields = [field.name for field in Book._meta.fields if field.name != "id"]
	readonly_fields = ['timestamp']
		
admin.site.register(Book, BookAdmin)
