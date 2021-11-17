from rest_framework import serializers
from .models import Class, ClassImages
from users.serializers import UserSerializer


class ClassSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()

    class Meta:
        model = Class
        fields = (
            "category",
            "title",
            "slug",
            "description",
            "teacher",
            "basic_price",
            "video",
            "images",
            "average_rating",
            "created",
            "updated",
        )
        depth = 1
