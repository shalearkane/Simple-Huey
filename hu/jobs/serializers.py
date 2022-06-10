from rest_framework import serializers
from jobs.models import job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = "__all__"
