from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'), # https://127.0.0.1:8000/
    path('categories/<int:catid>/', categories), # https://127.0.0.1:8000/categories/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]