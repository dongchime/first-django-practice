from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']  # title, text 필드에 관해서 입력을 받겠다.


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

