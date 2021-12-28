from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User
# 1.serializer

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=400)

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)


# 2. Model Serializer


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "description"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field=["id","username","password"]