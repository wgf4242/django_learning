from rest_framework import viewsets

from apps.mdself.models import Category
from apps.mdself.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
