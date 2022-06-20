from django.shortcuts import render
from apps.post.models import *
# Create your views here.
def index(request):
    news_all = Post.objects.all()
    category_all = Category.objects.all()
    context = {
        'news_all':news_all,
        'category_all':category_all,
    }
    return render(request, 'home-style-one.html', context)