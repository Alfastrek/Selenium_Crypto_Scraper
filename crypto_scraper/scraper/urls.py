from django.urls import path
from . import views

urlpatterns = [
    path('api/taskmanager/start_scraping', views.start_scraping, name='start_scraping'),
    path('api/taskmanager/scraping_status/<uuid:job_id>/', views.scraping_status, name='scraping_status'),
]
