from django.forms import ModelForm
from models import Comment, Article

class CommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['Text']
    def __init__(self, *args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['Text'].widget.attrs.update({'class' : 'form-control','style' : 'max-width: 50%;','rows': '4'})


class ArticleForm (ModelForm):
    class Meta:
        model = Article
        fields = ['Title', 'Text', 'Pic', 'Category']
    def __init__(self, *args,**kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['Title'].widget.attrs.update({'class': 'form-control form-group'})
        self.fields['Text'].widget.attrs.update({'class': 'form-control form-group'})
        self.fields['Pic'].widget.attrs.update({'class': 'form-control form-group'})
        self.fields['Category'].widget.attrs.update({'class': 'form-control form-group'})