from django.urls import path
from jobs.views import AddOne

urlpatterns = [
    # Comment CRUD
    path("add/", AddOne.as_view(), name="add-job"),
]
