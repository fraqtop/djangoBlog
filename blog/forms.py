from django.forms import ModelForm
from models import Comment

class CommentForm (ModelForm):
    class Meta:
        model = Comment
        fields = ['Text']
    def __init__(self, *args,**kwargs):
        super(CommentForm, self).__init__(*args,**kwargs)
        self.fields['Text'].widget.attrs.update({'class' : 'form-control','cols' : '4', 'rows' : '4'})