from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .forms import *

from django.shortcuts import get_object_or_404



# Create your views here.


class BlogView(ListView):
    template_name = 'blog.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created')[:3]

        return context


class SinBlogView(DetailView):
    template_name = 'single-blog.html'
    model = Post
    context_object_name = 'post'

    def post(self, request, pk):
        post = Post.objects.get(id=pk)

        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)

        return redirect('sin_blog',pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        index = list(posts).index(self.object)
        context['posts'] = posts
        try:
            context['previous'] = posts[index - 1]
        except:
            context['previous'] = posts[index]
        try:
            context['next'] = posts[index + 1]
        except:
            context['previous'] = posts[index]

        context['categories'] = Category.objects.all()
        context['recent'] = Post.objects.all().order_by('-created')[:3]

        try:
            context['best'] = Coments.objects.filter(Q(post=self.object) & Q(best_comment=True))[0]
        except:
            context['best'] = Coments.objects.filter(post=self.object)

        context['comment'] = Coments.objects.filter(post=self.object)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.like.filter(id=self.request.user.id).exists():
            liked = True
        context['num_of_like'] = likes_connected.num_of_likes()
        context['post_is_liked'] = liked

        return context
