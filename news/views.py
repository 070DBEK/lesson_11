from django.shortcuts import render, redirect, get_object_or_404
from .models import New


def home(request):
    posts = New.objects.all()
    ctx = {'posts': posts}
    return render(request, 'index.html', ctx)


def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        category = request.POST.get('category')
        if title and short_content and long_content and author and category:
            New.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                author=author,
                category=category
            )
            return redirect('home')
    return render(request, 'post/add-news.html')

def post_detail(request, post_id):
    posts = get_object_or_404(New, pk=post_id)
    ctx = {'posts': posts}
    return render(request, 'post/detail.html', ctx)

def post_by_category(request, category):
    posts = New.objects.filter(category=category)
    ctx = {'posts': posts, 'category': category}
    return render(request, 'post/news-by-category.html', ctx)
