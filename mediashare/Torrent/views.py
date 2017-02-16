from django.shortcuts import render
from .models import Torrent
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from rest_framework import generics
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    torrent_list = Torrent.objects.order_by('id')
    template = loader.get_template('Torrent/index.html')
    paginator = Paginator(torrent_list, 100)

    page = request.GET.get('page')
    try:
        torrent = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        torrent = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        torrent = paginator.page(paginator.num_pages)
    no_of_pages = paginator.num_pages+1
    page_range = range(1,no_of_pages)
    context = {
        'torrent': torrent,
    }
    return HttpResponse(template.render(context, request))



def search(request):
    query = request.GET['query']
    torrents_list = Torrent.objects.filter(Q(title__icontains=query) | Q(category__icontains=query)).order_by('title')
    user = request.user
    template = loader.get_template('Torrent/search.html')
    paginator = Paginator(torrents_list, 100)

    page = request.GET.get('page')
    try:
        torrent = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        torrent = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        torrent = paginator.page(paginator.num_pages)
    no_of_pages = paginator.num_pages+1
    page_range = range(1,no_of_pages)
    context = {
        'torrent': torrent,
        'query': query,
    }
    return HttpResponse(template.render(context, request))