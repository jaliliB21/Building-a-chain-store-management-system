from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import NewsForm
from .models import News


@login_required
def news(request):
    if not request.user.is_authenticated:
        return redirect('main:home')
    
    news = News.objects.all()

    return render(request, 'news/news.html', {
        'news': news
    })


@login_required
def add_news(request):

    title = 'Add news'

    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            news = form.save(commit=False)
            news.created_by = request.user
            news.save()

            return redirect('news:news')
    else:
        form = NewsForm()
    
    return render(request, 'news/add_news.html', {
        'form': form,
        'title': title,
    })


@login_required
def detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    return render(request, 'news/detail.html', {
        'news': news,
    })


@login_required
def edit(request, pk):

    title = 'Edit'

    if not request.user.is_authenticated:
        return redirect('news:detail', pk=pk)
    
    news = get_object_or_404(News, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)

        if form .is_valid():
            form.save()

            return redirect('news:detail', pk=pk)
    else:
        form = NewsForm(instance=news)

    return render(request, 'news/add_news.html', {
        'form': form,
        'title': title,
    })


@login_required
def delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('news:detail', pk=pk)
    
    news = get_object_or_404(News, pk=pk, created_by=request.user)
    news.delete()
    return redirect('news:news')