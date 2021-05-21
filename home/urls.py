from django.urls import path
from .views import *

app_name = "home"


urlpatterns = [
    path("", index.as_view(), name="index"),
    path("results/", Results, name="results")
]
