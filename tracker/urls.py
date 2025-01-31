from tracker.views import *
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("delete-Transaction/<uuid>/", deleteTransaction, name="deleteTransaction"),
]
