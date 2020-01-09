from rest_framework import serializers
from app_restFramework.models import *
from app_restFramework.views import *

class BookSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source = 'owner.username')

	class Meta:
		model = Book
		fields = ('name', 'author', 'publisher', 'time', 'owner')

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

class UserSerializer(serializers.HyperlinkedModelSerializer):
	books = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'book-detail')

	class Meta:
		model = User
		fields = ('id', 'username', 'books')
		