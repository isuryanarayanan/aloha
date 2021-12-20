from django.urls import path
from organizer.views import EventView,EventDetailView

urlpatterns = [
        path("event/",EventView, name="event-view"),
        path("event/<str:pk>/",EventDetailView, name="event-detail-view")
]
