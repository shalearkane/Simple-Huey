from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from huey.contrib import djhuey as huey
from jobs.models import job
from jobs.serializers import JobSerializer

# Create your views here.


def printOnePlusOne():
    print("1 + 1 = ")
    print(1 + 1)


class AddOne(GenericAPIView):
    serializer_class = JobSerializer
    model = job

    def post(self, request):
        printOnePlusOne()
        return Response(
            {"message": "Password reset email sent"}, status=status.HTTP_200_OK
        )
