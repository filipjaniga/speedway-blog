from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import markdown

from .models import Post, Comment
from .forms import CommentForm, PostForm


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 7
    login_url = reverse_lazy('login')


class PostDetailsView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    login_url = reverse_lazy('login')

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class = PostForm
    # fields = ['title', 'body']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = PostForm
    login_url = reverse_lazy('login')
    raise_exception = True

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_success_url(self):
        return reverse('blog_home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_superuser:
            return True
        return False

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

def handler403(request, exception):
    return render(request, 'blog/403.html', status=403)
