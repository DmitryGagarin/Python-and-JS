from .models import *


menu = [{'title': 'About', 'url_name': 'about'},
{'title': 'Add Article', 'url_name': 'addpage'},   
{'title': 'Feedback', 'url_name': 'feedback'},
{'title': 'Registration', 'url_name':'registration'},
{'title': 'Login', 'url_name': 'login'},
]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
    
    
    
