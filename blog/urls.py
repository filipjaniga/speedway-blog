from django.urls import path
from .views import homeView, postDetailsView, addPostView, deletePostView, updatePostView


urlpatterns = [
    path('', homeView.as_view(), name='blog_home'),
    path('post/<slug:slug>', postDetailsView.as_view(), name='details'),
    path('add_post', addPostView.as_view(), name='add_post'),
    path('post/<int:pk>/delete', deletePostView.as_view(), name='delete'),
    path('post/<int:pk>/update', updatePostView.as_view(), name='update')
]