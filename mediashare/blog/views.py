from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.template import loader
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages


def index(request):
    post_list = Post.objects.all().order_by('-date')
    template = loader.get_template('blog/index.html')
    paginator = Paginator(post_list, 20)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))