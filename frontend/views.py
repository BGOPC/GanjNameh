from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
