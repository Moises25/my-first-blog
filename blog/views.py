from django.shortcuts import render
from django.utils import timezone
from .models import Post #Agregamos nuestro modelo Post

# Create your views here.

def post_list(request): #creamos una funcion post_list
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#hacemos una query
        return render(request, 'blog/post_list.html', {'posts': posts}) #creamos nuestra vista
