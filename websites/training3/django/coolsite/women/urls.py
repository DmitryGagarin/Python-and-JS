from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), # https://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('feedback/', feedback, name='feedback'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]