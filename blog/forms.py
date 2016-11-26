from django import forms
from .models import Post

class PostForm(forms.ModelForm): #creamos un formulario PostForm tipo ModelForm
    class Meta:
        model = Post
        fields = ('title', 'text',)
