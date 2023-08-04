from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_months, name="challenge_path"),
    path("<int:month>", views.handle_monthly_num_challenge),
    path("<str:month>", views.handle_monthly_challenge, name='month-challenge')
]
