from rest_framework import serializers

from .models import Category, SubCategory


class SubCategoryNavSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("title", "slug")


class CategoryNavSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryNavSerializer(many=True)

    class Meta:
        model = Category
        fields = ("title", "slug", "sub_categories")


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"
