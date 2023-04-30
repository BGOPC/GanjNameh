from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("Booklets", views.BookletsView.as_view(), name="booklets-page"),
    path("Booklets/Booklet/<int:booklet_id>", views.BookletsView.as_view(), name="booklet-page"),
    path("Journals", views.JournalsView.as_view(), name="journals-page"),
    path("Booklets/Booklet/<int:journal_id>", views.JournalView.as_view(), name="journal-page"),
    path("support", views.SupportView.as_view(), name="support"),
]
