from django.urls import path

from .views import detail_view, list_view, add_post_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('new/', add_post_view, name="add_post")
]
