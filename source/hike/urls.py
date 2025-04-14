from django.urls import path
from .views import *

urlpatterns = [
    path("", index_view, name="hike"),
    path("wiltz", wiltz_view, name='hike-main'),
    path("unlock_hint/<int:route_progress_pk>", get_hint, name = "unlock_hint")
]