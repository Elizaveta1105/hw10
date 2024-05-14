from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Count
import logging

from .forms import QuotesForm, AuthorForm
from .models import Quote, Author, Tag

logger = logging.getLogger(__name__)


def main(request, page=1):
    if request.user.is_authenticated:
        quotes = Quote.objects.filter(Q(user=request.user) | Q(user=None)).order_by('-created_at')
    else:
        quotes = Quote.objects.filter(user=None).order_by('-created_at')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)

    top_ten_tags = Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]

    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page, 'tags': top_ten_tags})


@login_required
def add(request):
    form = QuotesForm(instance=Quote(), user=request.user)
    if request.method == 'POST':
        form = QuotesForm(request.POST, instance=Quote(), user=request.user)
        if form.is_valid():
            qu = form.save()
            qu.user = request.user
            qu.save()
            return redirect(to="quotes:main")

    return render(request, 'quotes/add.html', context={"form": form})


def get_author(request, author_name):
    author = Author.objects.get(fullname=author_name)
    return render(request, 'quotes/author.html', context={"author": author})


@login_required
def add_author(request):
    form = AuthorForm(instance=Author())
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            try:
                aut = form.save()
                aut.user = request.user
                aut.save()
                return redirect(to="quotes:add")
            except Exception as e:
                logger.error("Error while adding author: %s", e)

    return render(request, 'quotes/add_author.html', context={"form": form})


def get_quotes_by_tag(request, tag_name):
    quotes = Quote.objects.filter(tags__name=tag_name)

    return render(request, 'quotes/quotes_by_tag.html', context={"quotes": quotes, "tag_name": tag_name})
