from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .tasks import scrape_coin_data
from .models import Job, Task
from uuid import UUID
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@api_view(['POST'])
def start_scraping(request):
    if request.method == 'POST':
        coins = request.data.get('coins', [])
        if not coins:
            return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)

        job = Job.objects.create()
        task_ids = []

        for coin in coins:
            task = Task.objects.create(job=job, coin=coin)
            task_ids.append(str(task.id))
            scrape_coin_data.delay(str(task.id))

        return Response({'job_id': str(job.id), 'task_ids': task_ids}, status=status.HTTP_200_OK)

@api_view(['GET'])
def scraping_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    tasks = []
    for task in job.tasks.all():
        tasks.append({
            'coin': task.coin,
            'output': task.output
        })
    response_data = {
        'job_id': str(job.id),
        'tasks': tasks
    }
    return JsonResponse(response_data)