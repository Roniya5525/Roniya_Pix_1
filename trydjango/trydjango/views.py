from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
import random
from django.template.loader import render_to_string
# Create your views here.



def home_view1(request, *args, **kwargs):
    
    article_queryset=Article.objects.all()
    sample_id = random.randint(1,10)
    obj = Article.objects.get(id=1)
    

    context = {
        "object_list":article_queryset,
        "object":obj,
        "title":obj.title,
        "id":obj.id,
        "content":obj.content,
        "author":obj.author
    }

    return render(request, 'home.html', context=context)
#     # Html_String= render_to_string('home.html',context=context)
#     # return HttpResponse(Html_String)
    # return HttpResponse("Hello Welcome")
    
       
    


    