from rest_framework import serializers
from app_restFramework.models import Book

# class BookSerializer(serializers.Serializer):
	# name = serializers.CharField()
	# author = serializers.CharField()
	# publisher = serializers.CharField()
	# time = serializers.CharField()

class BookSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source = 'owner.username')

	class Meta:
		model = Book
		fields = ('name', 'author', 'publisher', 'time', 'owner')

	# no longer compatible 
	# def restore_object(self, attrs, instance=None):
	# 	if instance:
	# 		instance.name = attrs['name']
	# 		instance.author = attrs['author']
	# 		instance.publisher = attrs['publisher']
	# 		instance.time = attrs['time']
	# 		return instance
	# 	return Book(**attrs)

	def create(self, validated_data):
	       print('BookSerializer create')
	       return Book.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
	     instance.name = validated_data.get('name', instance.name)
	     instance.author = validated_data.get('author', instance.author)
	     instance.publisher = validated_data.get('publisher', instance.publisher)
	     instance.time = validated_data.get('time', instance.time)
	     # instance.created = validated_data.get('created', instance.created)
	     instance.save()
	     return instance

from app_restFramework.models import Book,User
class UserSerializer(serializers.ModelSerializer):
	# If you want to use books in the serializers, you can do this in the Book model:
	# owner = models.ManyToManyField(User, related_name="books")
	# book_set = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
	books = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

	class Meta:
		model = User
		fields = ('id', 'username', 'books')
		