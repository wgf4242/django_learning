from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
class Book(models.Model):
	added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_add')
	last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='book_edit')
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=200, null=True, blank=True)
	slug = models.SlugField(unique=True)
	publication_date = models.DateField(blank=True,null=True)
	updated = models.DateField(blank=True,null=True)
	timestamp = models.DateTimeField(auto_now_add=True,)
	# timestamp = models.DateField(blank=True,null=True)

	class Meta:
		ordering = ["-timestamp", "updated"]
		# unique_together = ["title", "slug"]

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
	    # url(r'^book/(?P<id>\d+)/$', BookDetail.as_view(), name='book_detail'),
		# return reverse("book_detail", kwargs={"id": self.id})
		return reverse("book_detail", kwargs={"slug": self.slug})

def pre_save_book(sender, instance, *args, **kwargs):
	slug = slugify(instance.title)
	instance.slug = slug

pre_save.connect(pre_save_book, sender=Book)