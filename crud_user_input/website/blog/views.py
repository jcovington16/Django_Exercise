from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post 

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'cov'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_new.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog_edit.html'
    fields = ['title', 'text']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    context_object_name = 'cov'
    success_url = reverse_lazy('home')
    