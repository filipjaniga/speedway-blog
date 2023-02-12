from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Post


class homeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 5

class postDetailsView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/article_details.html'
    login_url = reverse_lazy('login')

class addPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = ['title', 'body']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body']
    login_url = reverse_lazy('login')
    raise_exception = True

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class deletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_success_url(self):
        return reverse('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def handler403(request, exception):
    return render(request, 'blog/403.html', status=403)
