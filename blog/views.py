from django.shortcuts import render
from .models import Post, Comment
from django.utils import timezone
from .form import CommentForm


def blog_list(request):
    blog_posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {
        'posts': blog_posts
    })


def blog_detail(request):
    this_post = Post.objects.get(id=request.GET.get('id'))
    comments = Comment.objects.filter(post=this_post)
    form = CommentForm()
    if 'comment' in request.POST:
        comment = request.POST.get('comment')
        comment = Comment(user=request.user, post = this_post, comment = comment)
        comment.save()
    return render(request, 'blog/blog_detail.html', {
        'post': this_post,
        'comments': comments,
        'form': form,
    })
