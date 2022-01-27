from distutils.command.clean import clean
import imp
from turtle import title
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields= ['title', 'content', 'author']
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs= Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Please pick another title.")

class ArticleFormOld(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=50)
    author = forms.CharField(max_length=20)

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned_data",cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the cat":
    #         raise forms.ValidationError('This title is taken.')
    #     print("title",title)
    #     return title

    def clean(self):
        cleaned_data=self.cleaned_data
        print('all data',cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the cat":
            self.add_error('title', 'This title is taken')
        if 'cat' in content or 'cat' in title.lower():
            self.add_error('content', 'cat is cannot be in content')
            raise forms.ValidationError('cat is not allowed')
        return cleaned_data