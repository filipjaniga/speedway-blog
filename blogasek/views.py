from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class homeView(ListView):
    model = Post
    template_name = 'blogasek/home.html'
    paginate_by = 5

class postDetailsView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogasek/article_details.html'
    login_url = reverse_lazy('login')

class addPostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogasek/add_post.html'
    fields = ['title', 'body']
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class updatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blogasek/update_post.html'
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
    template_name = 'blogasek/delete_post.html'
    login_url = reverse_lazy('login')
    raise_exception = True

    def get_success_url(self):
        return reverse('home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





