from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Cats
from .forms import CatsForm
# Create your views here.
def index(request):
    """Домашняя страница приложения cats_blog"""
    return render(request, 'cats/index.html')
@login_required
def cats(request):
    """ВЫводит список котов."""
    cats = Cats.objects.filter(owner=request.user).order_by('date_added')
    context = {'cats': cats}
    return render(request, 'cats/cats.html', context)
@login_required
def new_cats(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = CatsForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CatsForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return redirect('cats:cats')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'cats/new_cats.html', context)
@login_required
def cat(request, cats_id):
    """выводит кота с характреристиками"""
    cats = Cats.objects.get(id=cats_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    if cats.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = CatsForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CatsForm(data=request.POST)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
            return redirect('cats:cat', cat_id=cats_id)
    # Вывести пустую или недействительную форму.
    context = {'cat': cats, 'form': form}
    return render(request, 'cats/cat.html', context)
@login_required
def edit_cats(request, cats_id):
    cats = Cats.objects.get(id=cats_id)
    if cats.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = CatsForm(instance=cats)
    else:
        form = CatsForm(request.POST, instance=cats)
        if form.is_valid():
            new_cat = form.save(commit=False)
            new_cat.owner = request.user
            new_cat.save()
        return redirect('cats:cat', cats_id=cats.id)

    context = {'cats': cats, 'form': form}
    return render(request, 'cats/edit_cats.html', context)
@login_required
def del_cats(request, cats_id):
    cats = Cats.objects.get(id=cats_id)
    cats.delete()
    return render(request, 'cats/cats.html',)
