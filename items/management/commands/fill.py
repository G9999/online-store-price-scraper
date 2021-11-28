# -*- coding: utf-8 -*-
import logging
import sys

from django.core.management.base import BaseCommand
from django.db.models import Q

from datetime import timedelta
from items.models import Price
from django.utils import timezone

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('reference_days_past', nargs='+', type=int)

    def handle(self, *args, **options):
        reference_days_past = int(options['reference_days_past'][0])
        today = timezone.now().date()
        today = today - timedelta(days=reference_days_past)
        yesterday = today - timedelta(days=1)
        for price in Price.objects.filter(date=today):
            defaults = {'price': price.price}
            Price.objects.get_or_create(date=yesterday, item=price.item, defaults=defaults)
