from django import forms
from datetime import date


# форма для добавления в БД новых авторов
class Form_add_author(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(
        label="Дата рождения",
        initial=format(date.today()),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    about = forms.CharField(label="Сведения об авторе",
                            widget=forms.Textarea)
    photo = forms.ImageField(label="Фото автора")
