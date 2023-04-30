from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from .models import Journal, Booklet


# Create your views here.

class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class Booklets(TemplateView):
    template_name = 'frontend/Booklet.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        all_booklets = Booklet.objects.all().order_by('-id')
        paginator = Paginator(all_booklets, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        booklets = page_obj.object_list
        context['booklets'] = booklets
        context['page_object'] = page_obj
        return context


class SupportView(TemplateView):
    template_name = "frontend/support.html"

    def get_context_daxta(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
