from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from apps.post.models import *
from django.db.models import Q
# Create your views here.

def news_views(request):
    if 'search_button' in request.GET:
        word = request.GET.get('search')
        search_products = Post.objects.filter(Q(title__icontains = word) | Q(description__icontains = word))
        return render(request, 'home/search_page.html', locals())
    else:
        news_all = Post.objects.all()
        category_all = Category.objects.all()

    return render(request, 'home-style-one.html', locals())


def post_op(request, id):
    if 'search_button' in request.GET:
        word = request.GET.get('search')
        search_products = Post.objects.filter(Q(title__icontains = word) | Q(description__icontains = word))
        return render(request, 'home/search_page.html', locals())
    else:

        post = Post.objects.get(id = id)
        tags = Tags.objects.all()
        return render(request, 'home/details-style-one.html', locals())