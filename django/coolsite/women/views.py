from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
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
    return HttpResponse('addpage page')

def feedback(request):
    return HttpResponse('feedback page')

def login(request):
    return HttpResponse('login page')

def show_post(request, post_id):
    return HttpResponse(f'Article with id {post_id}')
    
def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    
    if len(posts) == 0:
        raise Http404('Page not found')
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Show by Categories',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


    
