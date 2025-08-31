from django import forms

class ArticleCommentForm(forms.Form):
    text = forms.CharField(label="Комментарий", max_length=200)

# class ArticleCommentForm(forms.Form):
#     class Meta:
#         model = Comment
#         fields = ['text']