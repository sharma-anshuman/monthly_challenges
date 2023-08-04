from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

goals = {
    "january": "Wake up at 5 every morning",
    "february": "Run 5kms every day at a moderate consistent pace",
    "march": "Do 20 push ups everyday",
    "april": "Learn django for 3 hours everyday",
    "may": "Reduce alcohol intake",
    "june": "Read books for at least 30 minutes a day",
    "july": "Drink more water 4-5 liters a day",
    "august": "Have some more fun",
    "september": "Try to learn french language",
    "october": "Reduce screen time by 1 hour",
    "november": "Spend more time with family",
    "december": "Meditate for 20 minutes daily"
}


def show_months(request):
    months = list(goals.keys())
    redirect_path = reverse("challenge_path")
    return render(request, "challenges/index.html", {
        "months": months,
        "path": redirect_path
    })


def handle_monthly_num_challenge(request, month):
    if 0 < month <= 12:
        curr_month = list(goals.keys())[month-1]
        redirect_path = reverse('month-challenge', args=[curr_month])  # challenges/curr_month
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("This month is not supported")


def handle_monthly_challenge(request, month):
    try:
        habit = goals[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "habit": habit
        })
    except HttpResponseNotFound:
        return HttpResponseNotFound("This month is not supported")
