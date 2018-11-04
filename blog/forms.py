from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']  # title, text 필드에 관해서 입력을 받겠다.
