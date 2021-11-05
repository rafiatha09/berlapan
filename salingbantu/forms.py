from django import forms
from salingbantu.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class FormComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')

        widgets = {
            'user': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
