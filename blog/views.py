from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from blog.models import Article, Comment
from django.http import JsonResponse
from django.template.context_processors import csrf
from forms import CommentForm, ArticleForm
from django.contrib import auth
# Create your views here.




def articles (request, art_category='All'):
    args = {}
    all_articles = Article.objects.all().order_by('Date').reverse()
    args['user'] = auth.get_user(request)
    args['title'] = 'Main wood page'
    if art_category == 'All':
        args['articles'] = all_articles
    else:
        args['articles'] = all_articles.filter(Category=art_category)
    cats = []
    for art in all_articles:
        if cats.count(art.Category) == 0:
            cats.append(art.Category)
    args['cats'] = cats
    return render_to_response('Index.html', args)


def thisone (request, article_id=1):
    if request.POST:
        frm = CommentForm(request.POST)
        if frm.is_valid():
            comment = frm.save(commit=False)
            comment.Owner_article = Article.objects.get(id=article_id)
            frm.save()
    args ={}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.all().filter(Owner_article=article_id)
    args['form'] = CommentForm()
    args['user'] = auth.get_user(request)
    args['title'] = args['article'].Title
    return render_to_response('article.html',args)


def add (request):
    args = {}
    args.update(csrf(request))
    args['title'] = 'new article'
    args['form'] = ArticleForm()
    if request.POST:
        frm = ArticleForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('/')
    return render_to_response('for_forms.html',args)


def like (request, article_id):
    art = Article.objects.get(id=article_id)
    art.Likes += 1
    art.save()
    return JsonResponse({'likes': str(art.Likes)})

