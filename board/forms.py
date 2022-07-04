import re

from django import forms
from django.core.exceptions import ValidationError

from .models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'row': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Title mustn't start with a number")
        return title


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('accept', )
        fields = ['text']
        widgets = {'news': forms.HiddenInput}

    def clean_text(self):
        text = self.cleaned_data['text']
        return text
