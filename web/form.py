


from django import forms
from .models import Comment, UserBook

class CommentForm(forms.ModelForm):
    model = Comment
    fields = 'comment'
    class Meta:
        model = Comment
        fields = {'comment': forms.Textarea(attrs={'class': 'form-control w-100'})}

class addBookForm(forms.ModelForm):
    model = UserBook
    fields = 'user'
    class Meta:
        model = UserBook
        fields = {'user': forms.ChoiceField() }
