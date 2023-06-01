from rest_framework import serializers


from .models import (
    Category,
    Comment,
    Post,
    Tag,
)


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели поста"""

    class Meta:
        model = Post
        fields = ['id', 'name', 'content', 'image', 'created_at', 'updated_at', 'author', 'category', 'tag']


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для модели категории"""

    class Meta:
        model = Category
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментарий"""

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'updated_at', 'post', 'user']


class TagSerializer(serializers.ModelSerializer):
    """Сериализатор для модели тега"""

    class Meta:
        model = Tag
        fields = ['id', 'name']