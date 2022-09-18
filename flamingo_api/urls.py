from django.urls import path

from .views import (
    TickerCreateView, TickerListView, TicketRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        '', TickerListView.as_view(), name='tickets'
    ),
    path(
        'create/', TickerCreateView.as_view(), name='ticket_create'
    ),
    path(
        '<int:ticket_id>/',
        TicketRetrieveUpdateDestroyView.as_view(),
        name='ticket_detail'
    ),
]
