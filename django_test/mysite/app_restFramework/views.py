# from django.http import HttpResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from app_restFramework.models import Book
# from app_restFramework.serializers import BookSerializer

# class JSONResponse(HttpResponse):
# 	def __init__(self, data, **kwargs):
# 		ret = JSONRenderer().renderers(data)
# 		kwargs['content-type'] = "application/json"
# 		super(JSONResponse, self).__init__(data, **kwargs)

# def book_list(request):
# 	book = Book.objects.all()
# 	ser = BookSerializer(book)
# 	return JSONResponse(ser.data)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_restFramework.models import Book
from app_restFramework.serializers import BookSerializer
from app_restFramework.permissions import IsOwnerOrReadOnly

@api_view(['GET', 'POST'])
def book_list(requset):
	if requset.method == 'GET':
		book = Book.objects.all()
		ser = BookSerializer(book, many=True)
		return Response(ser.data)
	elif requset.method == 'POST':
		ser = BookSerializer(data=requset.data)
		print(requset.data)
		if ser.is_valid():
			ser.save()
			return Response(ser.data, status = status.HTTP_201_CREATED)
		else:
			return Response(ser.errors, status = status.HTTP_400_BAD_REQUEST)

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app_restFramework.models import Book
from app_restFramework.serializers import *
from rest_framework import generics
from rest_framework import permissions

class BookList(generics.ListCreateAPIView):
	q = Book.objects.all()
	serializer_class = BookSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly)

	def pre_save(self, object):
		object.owner = self.request.user
		

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	q = Book.objects.all()
	serializer_class = BookSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

from app_restFramework.serializers import BookSerializer, UserSerializer
from app_restFramework.models import User
class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
