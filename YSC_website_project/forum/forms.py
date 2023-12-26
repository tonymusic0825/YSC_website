from django import forms
from .models import Post

class CreateForumPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']