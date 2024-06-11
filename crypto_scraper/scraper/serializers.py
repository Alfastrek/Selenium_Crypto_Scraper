from rest_framework import serializers
from .models import Job, Task

class StartScrapingSerializer(serializers.Serializer):
    coins = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=False
    )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['coin', 'output']