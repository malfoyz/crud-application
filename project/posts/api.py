from rest_framework import viewsets

from .models import (
    Category,
    Comment,
    Post,
    Tag,
)
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    PostSerializer,
    TagSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """API ендпоинт для постов"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """API ендпоинт для категорий"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    """API ендпоинт для комментариев"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
    """API ендпоинт для тегов"""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer