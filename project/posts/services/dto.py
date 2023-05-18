from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class TagDTO:
    """DTO-класс для представления тега в приложении.

    Атрибуты:
    ----------
    id: int
        Идентификатор тега.
    name: str
        Название тега.
    """

    id: int
    name: str


@dataclass
class CategoryDTO:
    """DTO-класс для представления категории в приложении.

    Атрибуты:
    ----------
    id : int
        Идентификатор категории.
    name : str
        Название категории.
    """

    id: int
    name: str

@dataclass
class UserDTO:
    """DTO-класс для представления пользователя в приложении.

    Атрибуты:
    ----------
    id: int
        Идентификатор пользователя.
    username: str
        Регистрационное имя пользователя.
    email: str
        Адрес электронной почты.
    first_name: str
        Настоящее имя пользователя.
    last_name: str
        Настоящая фамилия пользователя.
    is_superuser: bool
        Является ли пользователь является суперпользователем.
    is_authenticated: bool
        Выполнил ли пользователь вход.
    """

    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool
    is_authenticated: bool


@dataclass
class CommentDTO:
    """DTO-класс для представления комментария.

    Атрибуты:
    ----------
    id : int
        Идентификатор комментария.
    text : str
        Текст комментария.
    created_at : datetime
        Дата и время создания комментария.
    updated_at : datetime
        Дата и время последнего обновления комментария.
    post_id: int
        Идентификатор поста, к которому принадлежит комментарий.
    user: UserDTO
        Пользователь, которому принадлежит комментарий.
    """

    id: int
    text: str
    created_at: datetime
    updated_at: datetime
    post_id: int
    user: UserDTO


@dataclass
class PostDTO:
    """DTO-класс для представления поста в приложении.

    Атрибуты:
    ----------
    id : int
        Идентификатор поста.
    name : str
        Название поста.
    content : str
        Текст поста.
    image : str
        Файловый путь к фото поста.
    created_at : datetime
        Дата и время создания поста.
    updated_at : datetime
        Дата и время последнего обновления поста.
    author : UserDTO
        Автор поста.
    category : int
        Ссылка на категорию поста.
    tags : List[str]
        Список тегов, относящихся к посту.
    """

    id: int
    name: str
    content: str
    image: str
    created_at: datetime
    updated_at: datetime
    author: UserDTO
    category: CategoryDTO
    tags: List[TagDTO]
