from django.shortcuts import render
from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'