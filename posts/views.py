from django.shortcuts import render
from django.views.generic import ListView
from .models import *

def home(request):
    context = {
        'colunas':Post.objects.all()
    }
    return render(request, 'posts/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'colunas'


def about(request):
    return render(request, 'posts/about.html', {'titulo':'about'})

