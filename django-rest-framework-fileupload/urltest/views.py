from django.shortcuts import render
from rest_framework import viewsets

from urltest.models import ImageModel
from urltest.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ImageModel.objects.all()
