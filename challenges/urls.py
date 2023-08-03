from django.urls import path
from . import views

urlpatterns = [
    path("<month>", views.handle_monthly_challenge)
]