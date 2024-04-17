from django.urls import path
from .views import HomeView, PostDetailsView, AddPostView, DeletePostView, UpdatePostView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name='blog_home'),
    path('post/<slug:slug>', PostDetailsView.as_view(), name='details'),
    path('add_post', AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update'),
    path('post/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment')
]