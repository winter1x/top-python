from django import forms
from .models import Comment

# class ArticleCommentForm(forms.Form):
#     text = forms.CharField(label="Комментарий", max_length=200, required=True)
#     email = forms.EmailField(required=True)
#     age = forms.IntegerField(min_value=0, max_value=120, required=False)

#     def clean_text(self):
#         text = self.cleaned_data['text']
#         if "спам" in text.lower():
#             raise forms.ValidationError(
#                 "Нельзя использовать спам в комментариях!"
#             )
#         return text

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

# class PasswordChangeForm(forms.Form):
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#     password_confirm = forms.CharField(widget=forms.PasswordInput, required=True)

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')

#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Пароли не совпадают!")

#         return cleaned_data