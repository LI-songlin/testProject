from django.urls import path
from . import views

urlpatterns = [
    # 首页时间线
    path('', views.timeline, name='timeline'),

    # Post 列表 API（Browsable API）
    path('api/posts/', views.PostListAPIView.as_view(), name='post-list-api'),
    path('post/new/', views.post_new, name='post_new'),
]


