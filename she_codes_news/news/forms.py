from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'img_url']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class':'title',
                    'placeholder':'...',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class':'content',
                    'placeholder':'...',
                }
            )
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'comment_text')
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'class':'comment_text',
                    'placeholder':'...',
                }
            )
        }