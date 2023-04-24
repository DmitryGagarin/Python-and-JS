from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), # https://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]