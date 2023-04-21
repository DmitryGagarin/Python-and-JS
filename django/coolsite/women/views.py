from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import * 


menu = ["About", "Add article", "Feedback", "Login"]


def index(request): 
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About Page'})

def categories(request, catid):   
    if(request.GET):
        print(request.GET)
    else:
        print("get quary is empty")
    return HttpResponse(f"<h1> Categories Page </h1> <p> {catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1> Archives Page </h1> <p> {year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1> Page Not Found </h1>")


    
