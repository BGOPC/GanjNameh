from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("support", views.SupportView.as_view(), name="support")
]
