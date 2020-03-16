from django import forms
from .models import Post, Terminal

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class TerminalForm(forms.ModelForm):
    class Meta:
        model = Terminal
        fields = ('eingabe', 'ausgabe')