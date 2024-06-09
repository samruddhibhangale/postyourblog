from django.shortcuts import render, get_object_or_404
from .models import Post
from .tasks import add

def post_list(request):
    result = add.delay(4, 6)
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
