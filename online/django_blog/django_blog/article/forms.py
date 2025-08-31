from django import forms
from .models import Comment
# class ArticleCommentForm(forms.Form):
#     text = forms.CharField(label="Комментарий", max_length=200)

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Комментарий',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Текст комментария'}),
        }

    def clean_content(self):
        content = self.cleaned_data['text']
        if "спам" in content.lower():
            raise forms.ValidationError(
                "Нельзя использовать спам в комментариях!"
            )
        return content