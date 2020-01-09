from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name

	class Meta:
	    ordering = ['name']
			

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	# email = models.EmailField(blank=True, verbose_name="e-mail")
	email = models.EmailField("e-mail", blank=True)

	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class BookManager(models.Manager):
	# self是 manager 本身
	def get_title(self, keyword):
		return self.filter(title__icontains = keyword).count()

class PyhtonBookManager(models.Manager):
	# 覆盖了就成了默认的。注意它的位置
	def get_query_set(self):
		# return super(PyhtonBookManager, self).get_query_set().filter(publisher__id = 6)	
		return super(PyhtonBookManager, self).get_query_set().filter(publisher__name__icontains = 'python')	

class Book(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(null=True, blank=True)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField(blank=True,null=True)
	
	objects = BookManager()
	python_objects = PyhtonBookManager()

	def checkAuthor(self):
		if 'a' in self.authors:
			return 'Hello World!'

	def __str__(self):
		return self.title

