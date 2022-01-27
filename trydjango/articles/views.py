from cgitb import lookup
from multiprocessing import context
import re
from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
from articles.models import Article
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
from django.http import Http404

# Create your views here.


def article_detail_view(request,slug=None):
    article_obj=None
    if slug is not None:
        try:
            article_obj=Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object":article_obj,
    }
    return render(request, 'article/detail.html', context=context)

@login_required
def article_create_view(request):
    form = ArticleForm
    context = {
        "form": form()
    }
    if request.method == "POST":
        form = ArticleForm(request.POST or None)
        context ={
            "form" : form
        } 
        if form.is_valid():
            article_object = form.save()
            context['form'] = ArticleForm()
            # return redirect("detail", slug=article_object.slug)
            return redirect(article_object.get_absolute_url())
            
    return render(request, 'article/create.html', context=context)

def article_search_view(request):
    query = request.GET.get('abc')
    qs = Article.objects.search(query=query)
    context = {
        "object_list" : qs
    }
    return render(request, 'article/search.html', context=context)