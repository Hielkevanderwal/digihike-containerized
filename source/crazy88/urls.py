from django.urls import path
from .views import *

urlpatterns = [
    path("",crazy88_view_home, name="crazy88_view"),
    path("<str:mission_list>/", crazy88_view_list, name="crazy88_view-list"),
    path("<str:mission_list>/<int:mission_number>", view_detailed_task, name="crazy88_view-detailed"),
]