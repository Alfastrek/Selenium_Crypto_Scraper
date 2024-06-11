from celery import shared_task
from .models import Task
from .coinmarketcap import CoinMarketCap 

@shared_task
def scrape_coin_data(task_id):
    try:
        task = Task.objects.get(id=task_id)
        coin = task.coin
        scraper = CoinMarketCap()
        output = scraper.fetch_coin_data(coin)
        task.output = output
        task.status = 'completed'
        task.save()
    except Task.DoesNotExist:
        pass 