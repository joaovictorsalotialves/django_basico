from typing import Any

from django.shortcuts import render
from django.http import HttpRequest, Http404

from blog.data import posts


def blog(request):
    context = {
        # 'text': 'BLOG',
        'title': 'Blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
        # 'text': 'BLOG',
        'title': f'Post - {found_post["title"]}',
        'post': found_post,
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def exemplo(request):
    context = {
        'text': 'BLOG / EXEMPLO',
        'title': 'Blog - Exemplo',

    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
