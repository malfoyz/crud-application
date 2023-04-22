from django.shortcuts import (
    render,
    redirect,
)
from django.http import (
    HttpRequest, 
    HttpResponse,
)

from .models import *
from .forms import *


def index(request: HttpRequest) -> HttpResponse:
    """Обработчик главной страницы"""

    categories = Category.objects.all()

    if 'category' in request.GET:
        cat_id = int(request.GET['category'])
        posts = Post.objects.filter(category__pk=cat_id)
        page_name = categories.get(pk=cat_id).name
    else:
        cat_id = 0
        posts = Post.objects.all()
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

    categories = Category.objects.all()
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=id)
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
        commentForm = CommentForm(initial={'post': post.pk, 'user': request.user.pk})
        context['form'] = commentForm
        return render(request, 'posts/post.html', context)


def create_post(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы создания поста"""

    categories = Category.objects.all()
    context = {
        'title': 'Добавление поста',  
        'categories': categories,
    }

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save()
            return redirect('posts:post', postForm.instance.pk)
        else:
            context['form'] = postForm
            return render(request, 'posts/edit_post.html', context)
    else:
        postForm = PostForm(initial={'author': request.user.pk })
        context['form'] = postForm
        return render(request, 'posts/edit_post.html', context)
    

def edit_post(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы изменения поста"""

    categories = Category.objects.all()
    post = Post.objects.get(pk=id)
    context = {
        'title': f'Изменение поста №{id}',
        'categories': categories,
    }

    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            postForm.save()
            return redirect('posts:post', id)
        else:
            context['form'] = postForm
            return render(request, 'posts/edit_post.html', context)
    else:
        postForm = PostForm(instance=post)
        context['form'] = postForm
        return render(request, 'posts/edit.html', context)
    

def delete_post(request: HttpRequest, id: int) -> HttpRequest:
    """Обработчик удаления поста"""

    post = Post.objects.get(pk=id)
    context = {
        'title': f'Удаление записи №{id}',
    }
    
    if request.method == 'POST':
        post.delete()
        return redirect('posts:home')
    else:
        return render(request, 'posts/confirm_delete.html', context)



def get_categories(request: HttpRequest) -> HttpResponse:
    """Обработчик страницы категорий"""

    categories = Category.objects.order_by('name')
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

    categories = Category.objects.all()
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

    categories = Category.objects.all()
    category = categories.get(pk=id)
    context = {
        'title': 'Изменение категории',
    }

    if request.method == 'POST':
        categoryForm = CategoryForm(request.POST, instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('posts:get_categories')
        else:
            context['form'] = categoryForm
            return render(request, 'posts/edit.html', context)
    else:
        categoryForm = CategoryForm(instance=category)
        context['form'] = categoryForm
        return render(request, 'posts/edit.html', context)
    

def delete_category(request: HttpRequest, id: int) -> HttpResponse:
    """Обработчик страницы подтверждения удаления категории"""

    category = Category.objects.get(pk=id)
    context = {
        'title': f'Удаление категории: {category.name}'
    }

    if request.method == 'POST':
        category.delete()
        return redirect('posts:get_categories')
    else:
        return render(request, 'posts/confirm_delete.html', context)