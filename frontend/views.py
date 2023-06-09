from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import View, TemplateView, FormView, CreateView
from . import forms
from .models import Journal, Booklet


# Create your views here.

class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class BookletsView(TemplateView):
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


class BookletView(TemplateView):
    template_name = "frontend/Booklet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        booklet_id = kwargs.get('booklet_id', -1)
        context['booklet'] = get_object_or_404(Booklet, id=booklet_id)
        return context


class UploadBookletView(CreateView):
    template_name = 'frontend/uploadBooklet.html'
    form_class = forms.UploadBookletForm
    success_url = reverse_lazy('booklet-page')

    def form_valid(self, form):
        booklet = form.save(commit=False)
        booklet.author = self.request.user
        booklet.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['files'] = self.request.FILES
        return kwargs

    def get_success_url(self):
        return reverse('booklet-page', args=[self.object.id])


class ContactView(FormView):
    template_name = "frontend/contact.html"
    form_class = forms.ContactForm
    success_url = reverse_lazy("home")


class JournalsView(TemplateView):
    template_name = 'frontend/Journals.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        all_journals = Journal.objects.all().order_by('-id')
        paginator = Paginator(all_journals, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        booklets = page_obj.object_list
        context['journals'] = booklets
        context['page_object'] = page_obj
        return context


class JournalView(TemplateView):
    template_name = "frontend/Journal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        journal_id = kwargs.get('journal_id', -1)
        context['journal'] = get_object_or_404(Journal, id=journal_id)
        return context
