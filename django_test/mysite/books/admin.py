from django.contrib import admin

# Register your models here.
from django.contrib import admin
from books.models import Publisher, Author, Book

# admin.site.register(Publisher)
# admin.site.register(Author)
# admin.site.register(Book)



class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	# fields = ('title', 'authors', 'publisher',)
	# fields = ('title', 'authors', 'publisher', 'publication_date')
	filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)

	# 管理员返回全部，普通用户返回 作者为user的书
	def get_queryset(self, request):
		qs = super(BookAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(author = request.user)

	def save_model(self, request, obj, form, change):
		if change:
			obj_original = self.model.objects.get(pk=obj.pk)
		else:
			obj_original = None
		obj.author = request.user
		obj.save()


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
