# testApp/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 根据你的 Post 模型字段来写，这里先假设只有 content 字段
        fields = ['content']
