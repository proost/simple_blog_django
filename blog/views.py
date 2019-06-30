from django.shortcuts import render,get_object_or_404,get_list_or_404
from blog.models import (Blogger,Post,Comment)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

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

class CommentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Comment
    fields = ['contents',]

    def get_context_data(self,**kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self,form):
        author = Blogger.objects.get(user=self.request.user)
        form.instance.author = author
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CommentCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})