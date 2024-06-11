from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Task
from .coinmarketcap import CoinMarketCap 
from .tasks import scrape_coin_data
from .serializers import TaskSerializer

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        job = Job.objects.create()

        for coin in coins:
            task = Task.objects.create(job=job, coin=coin)
            scrape_coin_data.delay(task.id)  

        return Response({'job_id': job.id}, status=status.HTTP_201_CREATED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            tasks = Task.objects.filter(job=job)
            serializer = TaskSerializer(tasks, many=True)
            return Response({'job_id': job.id, 'tasks': serializer.data}, status=status.HTTP_200_OK)
        except Job.DoesNotExist:
            return Response({'error': 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
