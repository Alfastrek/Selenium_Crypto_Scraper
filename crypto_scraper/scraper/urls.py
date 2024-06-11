from django.urls import path
from .views import StartScrapingView, ScrapingStatusView

urlpatterns = [
    path('api/taskmanager/start_scraping', StartScrapingView.as_view(), name='start_scraping'),
    path('api/taskmanager/scraping_status/<uuid:job_id>', ScrapingStatusView.as_view(), name='scraping_status'),
]
