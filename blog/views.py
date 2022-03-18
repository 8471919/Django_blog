from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request) :
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    #Post의 pk의 값이 매개변수로받은 pk와 같은 것을 뽑아온다.
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )