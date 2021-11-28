from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Price


def index(request):
    last_day_obj = Price.objects.all().order_by('-date').first()
    last_day = last_day_obj.date

    first_day = last_day - timedelta(days=30)
    first_day_db = Price.objects.filter(date__gte=first_day).order_by('date').first().date
    # retrieve either the last 30 days or either the first one in the DB
    first_day = max(first_day_db, first_day)

    days = []
    current_day = first_day

    while current_day <= last_day:
        days.append(current_day)
        current_day = current_day + timedelta(days=1)

    items = Item.objects.all().order_by('current_price')

    prices = {}

    for item in items:
        item_prices = [item.date_price(day) for day in days]
        prices[item.pk] = item_prices

    data = {
        'days': days,
        'items': items,
        'prices': prices,
    }

    return render(request, 'index.haml', data)
