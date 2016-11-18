from django.shortcuts import render

# Create your views here.

def post_list(request): #creamos una funcion post_list
        return render(request, 'blog/post_list.html', {}) #creamos nuestra vista
