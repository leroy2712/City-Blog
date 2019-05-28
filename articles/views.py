from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def articles_list(request):
    articles = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'articles/articles_list.html', {'articles': articles})

def article_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('/')

    else:
        form = PostForm()
        return render(request, 'articles/article_new.html', {'form': form})