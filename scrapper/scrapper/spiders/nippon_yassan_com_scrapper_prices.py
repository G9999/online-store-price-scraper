from decimal import Decimal
from django.utils import timezone

import scrapy
from scrapy.http import FormRequest

from items.models import Item, Price

date = timezone.now().date()


class NipponYassanComSpiderName(scrapy.Spider):
    total_books = 0
    row_num = 0
    name = 'nippon_yassan_com_scrapper_prices'

    # start_urls = [item.url for item in Item.objects.all()[:1]]

    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
    }

    def start_requests(self):
        return [
            FormRequest(item.url, formdata={'id_currency': '2', 'SubmitCurrency': ''}, callback=self.parse) for item in Item.objects.all()
        ]


    def parse(self, response):
        name = response.xpath('.//div[@id="pb-left-column"]/h1[@class="title"]/text()').extract()[0]
        price = response.xpath('.//span[@id="our_price_display"]/text()').extract()[0]

        if price[0] == '$':
            price = Decimal(price.replace('$', ''))

            item = Item.objects.get(url=response.url)

            defaults = {'price': price}
            _, _ = Price.objects.get_or_create(item=item, date=date, defaults=defaults)

            item.current_price = price
            item.save(update_fields=['current_price'])

    def _val(self, extractor, sep=' '):
        # from HTMLParser import HTMLParser
        # h = HTMLParser()
        valid_str = []
        insert = False
        for val in extractor.extract():
            # val = h.unescape(val)
            val = val.replace('\r', '').replace('\n\n', '\n').strip()
            # val = re.sub(' +', ' ', val)
            if '\n' in val:
                val = val.strip() + '\n'
            if not insert:
                val = val.strip()
            if len(val) > 0:
                # print '-val-'
                # print '-'+val+'-'
                valid_str.append(val)
                insert = True

        return sep.join(valid_str).strip()
