from django import forms
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    title = forms.CharField(min_length=6)

    class Meta:
        model = Post
        fields = ['author', 'type', 'title', 'text']
        labels = {'author':'Автор', 'type':'Категория', 'title':'Заголовок', 'text':'Текст публикации'}


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if text == title:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data