from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import * 
from .models import * 
from .utils import *

class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Main Page")
        return dict(list(context.items()) + list(c_def.items()))
        
    def get_queryset(self):
        return Women.objects.filter(is_published=True)
    
    
    
def about(request):
    contact_list = Women.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'About Page'})

class AddPage(LoginRequiredMixin,  DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Add Page")        
        return dict(list(context.items()) + list(c_def.items()))

def feedback(request):
   return render(request, 'women/feedback.html', {'menu': menu, 'title': 'Feedback Page'})

def registration(request):
    return render(request, 'women/registration.html', {'menu': menu, 'title': 'Registration'})


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context["post"])        
        return dict(list(context.items()) + list(c_def.items()))

class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    
    def get_queryset(self):
        return Women.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Category - ' + str(context['posts'][0].cat),
                                      cat_selected = context['posts'][0].cat_id)        
        return dict(list(context.items()) + list(c_def.items()))
    
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'women/registration.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Registration')
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'women/login.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Login')
        return dict(list(context.items()) + list(c_def.items())) 
    
def logout_user(request):
    logout(request)
    return redirect('login')