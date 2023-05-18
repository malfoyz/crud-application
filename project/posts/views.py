from django.shortcuts import (
    render,
    redirect,
)
from django.http import (
    HttpRequest, 
    HttpResponse,
)

from .models import Category, Comment, Post
from .services.dao import CategoryDAO, CommentDAO, PostDAO
from .forms import CategoryForm, CommentForm, PostForm


categoryDAO = CategoryDAO()
postDAO = PostDAO()
commentDAO = CommentDAO()


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы"""

    categories = categoryDAO.get_all()

    if 'category' in request.GET:
        cat_id = int(request.GET['category'])
        posts = postDAO.get_by_category(cat_id)
        page_name = categoryDAO.get_by_id(cat_id).name
    else:
        cat_id = 0
        posts = postDAO.get_all()
        page_name = 'Все посты'

    context = {
        'title': page_name,
        'posts': posts,
        'categories': categories,
        'cat_id': cat_id,
    }

    return render(request, 'posts/posts.html', context)


def get_post(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы поста"""

    categories = categoryDAO.get_all()
    post = postDAO.get_by_id(id)
    comments = commentDAO.filter_by_post_id(id)
    context = {
        'categories': categories,
        'post': post,
        'comments': comments,
    }

    if request.method == 'POST':
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save()
            return redirect('posts:get_post', id)
        else:
            context['form'] = commentForm
            return redirect('posts:get_post', id)
    else:
        commentForm = CommentForm(initial={'post': post.id, 'user': request.user.pk})
        context['form'] = commentForm
        return render(request, 'posts/post.html', context)


def create_post(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы создания поста"""

    categories = categoryDAO.get_all()
    context = {
        'title': 'Добавление поста',  
        'categories': categories,
    }

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save()
            return redirect('posts:get_post', postForm.instance.pk)
        else:
            context['form'] = postForm
            return render(request, 'posts/edit.html', context)
    else:
        postForm = PostForm(initial={'author': request.user.pk})
        context['form'] = postForm
        return render(request, 'posts/edit.html', context)


def edit_post(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы изменения поста"""

    categories = categoryDAO.get_all()
    post = postDAO.get_by_id(id)
    post_orm = Post.objects.get(pk=id)
    context = {
        'title': f'Изменение поста №{id}',
        'categories': categories,
    }

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post_orm)
        if postForm.is_valid():
            postForm.save()
            return redirect('posts:get_post', id)
        else:
            context['form'] = postForm
            return render(request, 'posts/edit_post.html', context)
    else:
        postForm = PostForm(instance=post_orm)
        context['form'] = postForm
        return render(request, 'posts/edit.html', context)
    

def delete_post(request: HttpRequest, id: int) -> HttpRequest:
    """Обработчик удаления поста"""

    context = {
        'title': f'Удаление записи №{id}',
    }

    if request.method == 'POST':
        postDAO.delete_by_id(id)
        return redirect('posts:home')
    else:
        return render(request, 'posts/confirm_delete.html', context)


def get_categories(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы категорий"""

    categories = categoryDAO.get_all()
    context = {
        'title': 'Категории',
        'categories': categories,
    }

    return render(
        request=request,
        template_name='posts/categories.html',
        context=context,
    )


def create_category(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы создания категории"""

    categories = categoryDAO.get_all()
    context = {
        'title': 'Создание категории',
        'categories': categories,
    }

    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('posts:get_categories')
        else:
            context['form'] = categoryForm
            return render(request, 'posts/edit.html', context)
    else:
        categoryForm = CategoryForm()
        context['form'] = categoryForm
        return render(request, 'posts/edit.html', context)


def edit_category(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы изменения категории"""

    categories = categoryDAO.get_all()
    category = categoryDAO.get_by_id(id)
    category_orm = Category.objects.get(pk=id)
    context = {
        'title': 'Изменение категории',
    }

    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST, instance=category_orm)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('posts:get_categories')
        else:
            context['form'] = categoryForm
            return render(request, 'posts/edit.html', context)
    else:
        categoryForm = CategoryForm(instance=category_ormit )
        context['form'] = categoryForm
        return render(request, 'posts/edit.html', context)


def delete_category(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы подтверждения удаления категории"""

    category = categoryDAO.get_by_id(id)
    context = {
        'title': f'Удаление категории: {category.name}'
    }

    if request.method == 'POST':
        categoryDAO.delete_by_id(id)
        return redirect('posts:get_categories')
    else:
        return render(request, 'posts/confirm_delete.html', context)