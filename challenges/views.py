from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november",
          "december"]

goals = [
    "Wake up at 5 every morning",
    "Run 5kms every day at a moderate consistent pace",
    "Do 20 pushups everyday",
    "Learn django for 3 hours everyday",
    "Reduce alcohol intake",
    "Read books for at least 30 mins a day",
    "Drink more water 4-5 liters a day",
    "Have some more fun",
    "Try to learn french language",
    "Reduce screen time by 1 hour",
    "Spend more time with family",
    "Meditate for 20 minutes daily"
]


def handle_monthly_challenge(request, month):
    for idx, current_month in enumerate(months):
        if current_month == month:
            return HttpResponse(goals[idx])
    return HttpResponse("This url is not supported")
