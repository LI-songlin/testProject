from django.shortcuts import render
from .models import Post

# 首页时间线视图
def timeline(request):
    query = request.GET.get('q')

    posts = Post.objects.select_related('author').all()

    if query:
        posts = posts.filter(content__icontains=query)

    posts = posts.order_by('-created_at')

    return render(request, 'timeline.html', {'posts': posts, 'query': query})




# 下面是 REST API 用的视图
from rest_framework import generics
from .serializers import PostSerializer

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 先不写数据库
            post.author = request.user      # 必填：作者
            post.save()
            return redirect('timeline')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

