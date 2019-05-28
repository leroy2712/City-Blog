from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def articles_list(request):
    articles = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'articles/articles_list.html', {'articles': articles})