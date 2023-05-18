from abc import ABC, abstractmethod
from typing import Iterable, List

from django.contrib.auth.models import User

from .dto import (CategoryDTO, CommentDTO,
                  PostDTO, TagDTO, UserDTO)
from ..models import Category, Comment, Post, Tag


class CategoryDAO:
    """DAO категории - отвечает за работу с хранилищем"""

    def __orm_to_dto(self, category_orm: Category) -> CategoryDTO:
        return CategoryDTO(
            id=category_orm.pk,
            name=category_orm.name,
        )

    def __orm_to_entities(self, categories_orm: Iterable[Category]) -> List[CategoryDTO]:
        return list(map(self.__orm_to_dto, categories_orm))

    def get_all(self) -> Iterable[CategoryDTO]:
        categories = Category.objects.all()
        return self.__orm_to_entities(categories)

    def get_by_id(self, category_id: int) -> CategoryDTO:
        category = Category.objects.get(pk=category_id)
        return self.__orm_to_dto(category)

    def delete_by_id(self, category_id: int) -> None:
        category = Category.objects.get(pk=category_id)
        category.delete()


class PostDAO:
    """DAO продукта - отвечает за работу с хранилищем"""

    def __orm_to_dto(self, post_orm: Post) -> PostDTO:
        tags = [TagDAO().get_by_id(tag.pk) for tag in post_orm.tag.all()]
        category = CategoryDAO().get_by_id(post_orm.category.pk)
        author = UserDAO().get_by_id(post_orm.author.pk)

        return PostDTO(
            id=post_orm.pk,
            name=post_orm.name,
            content=post_orm.content,
            image=post_orm.image,
            created_at=post_orm.created_at,
            updated_at=post_orm.updated_at,
            author=author,
            category=category,
            tags=tags,
        )

    def __orm_to_entities(self, posts_orm: Iterable[Post]) -> Iterable[PostDTO]:
        return map(self.__orm_to_dto, posts_orm)

    def get_all(self) -> Iterable[PostDTO]:
        posts = Post.objects.all()
        return self.__orm_to_entities(posts)

    def get_by_category(self, category_id: int) -> Iterable[PostDTO]:
        posts = Post.objects.filter(category__pk=category_id)
        return self.__orm_to_entities(posts)

    def get_by_id(self, post_id: int) -> PostDTO:
        post = Post.objects.get(pk=post_id)
        return self.__orm_to_dto(post)

    def delete_by_id(self, post_id) -> None:
        post = Post.objects.get(pk=post_id)
        post.delete()


class TagDAO:
    """DAO тега - отвечает за работу с храналищем"""

    def __orm_to_dto(self, tag_orm: Tag) -> TagDTO:
        return TagDTO(
            id=tag_orm.pk,
            name=tag_orm.name,
        )

    def __orm_to_entities(self, tags_orm: Iterable[Tag]) -> Iterable[TagDTO]:
        return map(self.__orm_to_dto, tags_orm)

    def get_by_id(self, id: int) -> TagDTO:
        tag = Tag.objects.get(pk=id)
        return tag


class UserDAO:
    """DAO пользователя - отвечает за работу с хранилищем"""

    def __orm_to_dto(self, user_orm: User) -> UserDTO:
        return UserDTO(
            id=user_orm.pk,
            username=user_orm.username,
            email=user_orm.email,
            first_name=user_orm.first_name,
            last_name=user_orm.last_name,
            is_superuser=user_orm.is_superuser,
            is_authenticated=user_orm.is_authenticated,
        )

    def get_by_id(self, user_id) -> UserDTO:
        user = User.objects.get(pk=user_id)
        return self.__orm_to_dto(user)


class CommentDAO:
    """DAO комментарий - отвечает за работу с хранилищем"""

    def __orm_to_dto(self, comment_orm: Comment) -> CommentDTO:
        user = UserDAO().get_by_id(comment_orm.user.pk)

        return CommentDTO(
            id=comment_orm.pk,
            text=comment_orm.text,
            created_at=comment_orm.created_at,
            updated_at=comment_orm.updated_at,
            post_id=comment_orm.post.pk,
            user=user,
        )

    def __orm_to_entities(self, comments_orm: Iterable[Comment]) -> Iterable[CommentDTO]:
        return map(self.__orm_to_dto, comments_orm)

    def filter_by_post_id(self, post_id: int) -> Iterable[CommentDTO]:
        comments = Comment.objects.filter(post=post_id)
        return self.__orm_to_entities(comments)
