from django.urls import path
from .views import render_posts, post_detail, posts

app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_detail, name='postdetail'),
    path('posts', posts, name='Posts2')
]