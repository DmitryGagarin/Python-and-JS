from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from .models import * 


menu = [{'title': 'About', 'url_name': 'about'},
{'title': 'Add Article', 'url_name': 'addpage'},   
{'title': 'Feedback', 'url_name': 'feedback'},
{'title': 'Login', 'url_name': 'login'}   
]


def index(request): 
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About Page'})

def addpage(request):
    return render(request, 'women/addpage.html', {'menu': menu, 'title': 'Addpage'})

def feedback(request):
   return render(request, 'women/feedback.html', {'menu': menu, 'title': 'Feedback Page'})

def login(request):
    return render(request, 'women/login.html', {'menu': menu, 'title': 'Login'})

def show_post(request, post_id):
    post = get_object_or_404(Women, pk=post_id)
    
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    
    return render(request, 'women/post.html', context=context)
        
def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    
    if len(posts) == 0:
        raise Http404('Page not found')
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Show by Categories',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)


    
