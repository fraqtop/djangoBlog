from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import Article, Comment
from django.http import JsonResponse
from django.template.context_processors import csrf
from forms import CommentForm
from django.contrib import auth
# Create your views here.




def articles (request):
    return render_to_response('Index.html',{'articles': Article.objects.all().order_by('Date').reverse(),
                                            'user': auth.get_user(request)})


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
    return render_to_response('article.html',args)


def like (request, article_id):
    art = Article.objects.get(id=article_id)
    art.Likes += 1
    art.save()
    return JsonResponse({'likes': str(art.Likes)})
