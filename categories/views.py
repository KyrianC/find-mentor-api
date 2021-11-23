from rest_framework import generics

from .models import Category, SubCategory
from .serializers import (
    CategoryNavSerializer,
    CategorySerializer,
    SubCategorySerializer,
)


class CategoryNavigation(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryNavSerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryList(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        parent = self.kwargs.get("parent")
        print(parent)
        return SubCategory.objects.filter(parent_category__slug=parent)
