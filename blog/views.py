from django.shortcuts import render
from blog.models import (Blogger,Post,Comment)
from django.views import generic

def index(request):
    num_posts = Post.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    context = {
        'num_posts': num_posts,
        'num_bloggers': num_bloggers
    }
    return render(request, 'index.html', context=context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

class PostDetailView(generic.DetailView):
    model = Post

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentCreateView(generic.CreateView):
    model = Comment
    fields = '__all__'
