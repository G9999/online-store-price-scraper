from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, blank=True)
    url = models.URLField(unique=True)
    keywords = models.CharField(max_length=100, blank=True)
    display = models.BooleanField(default=True)

    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @property
    def last_price(self):
        last_price = self.price_set.all().order_by('-date').first()
        if last_price:
            return last_price.price
        else:
            return ''

    @property
    def price_variation(self):
        last_prices = self.price_set.all().order_by('-date')[:2]
        if len(last_prices) == 2:
            last_price, second_to_last_price = last_prices
            price_variation = (last_price.price - second_to_last_price.price) / second_to_last_price.price
            return '%s%%' % round((price_variation*100), 2)
        else:
            return ''

    def __unicode__(self):
        return self.name

    def date_price(self, date):
        date_price = self.price_set.filter(date=date).first()
        if date_price:
            return date_price.price
        else:
            return ''


class Price(models.Model):
    item = models.ForeignKey(Item)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    date = models.DateField()

    class Meta:
        unique_together = ('item', 'date')
