from django.urls import path
from organizer.views import EventView,EventDetailView, EventAdminDetailView

urlpatterns = [
        path("event/",EventView, name="event-view"),
        path("event/registered/<str:pk>",EventAdminDetailView, name="event-admin-view"),
        path("event/<str:pk>/",EventDetailView, name="event-detail-view")
]
