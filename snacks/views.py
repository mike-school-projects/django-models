from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fruits"] = ['apple', 'banana', 'peach']
        return context

class SnackListPageView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snacks'

class SnackDetailPageView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    context_object_name = 'snacks'