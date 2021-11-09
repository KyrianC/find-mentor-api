from rest_framework import generics

from .models import Category
from .serializers import CategoryNavSerializer, CategorySerializer


class CategoryNavigation(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryNavSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
