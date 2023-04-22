from django import forms

from .models import *


class PostForm(forms.ModelForm):
    """Форма поста, связанная с моделью"""

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'author': forms.HiddenInput()}


class CategoryForm(forms.ModelForm):
    """Форма категории, связанная с моделью"""

    class Meta:
        model = Category
        fields = '__all__'

class CommentForm(forms.ModelForm):
    """Форма комментария, связанная с моделью"""

    class Meta:
        model = Comment
        fields = '__all__'
        labels = {'text': 'Введите комментарий'}
        widgets = {
            'post': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }