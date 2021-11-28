# sell script to run the scrapper. It can be used with cron to run it daily
source venv/bin/activate
cd scrapper/
scrapy crawl nippon_yassan_com_scrapper_prices
