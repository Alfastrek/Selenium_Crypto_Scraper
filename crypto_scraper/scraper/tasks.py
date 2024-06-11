from celery import shared_task
from .coinmarketcap import CoinMarketCap
from .models import Task

@shared_task
def scrape_coin_data(task_id):
    try:
        task = Task.objects.get(id=task_id)
        cmc = CoinMarketCap()
        coin_data = cmc.fetch_coin_data(task.coin)
        cmc.close()
        task.output = coin_data
        task.status = 'completed'
        task.save()
    except Exception as e:
        task.status = 'failed'
        task.output = {'error': str(e)}
        task.save()