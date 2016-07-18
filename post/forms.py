# coding: utf-8
from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
        fields = ('title', 'slug', 'category', 'picture', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите название'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Укажите slug'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'picture': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('Минимум 8 символов')
        return title

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if len(slug) < 5:
            raise forms.ValidationError('Минимум 8 символов')
        return slug

    def clean_picture(self):
        picture = self.cleaned_data.get('picture', False)
        if picture:
            if picture.size > 1 * 1024 * 1024:
                raise forms.ValidationError('Картинка должна быть максимум 1 мгбайт')
            return picture
        else:
            raise forms.ValidationError('Не могу загрузить картинку')

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 15:
            raise forms.ValidationError('Тест должен содержать как минимум одно предложение')
        return text

