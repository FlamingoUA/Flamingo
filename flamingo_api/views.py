from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework import permissions, filters
from rest_framework.pagination import PageNumberPagination

from model.models import Ticket
from .serializers import TicketSerializer


class TickerCreateView(CreateAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class TickerListView(ListAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['price']


class TicketRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TicketSerializer
    lookup_url_kwarg = 'ticket_id'
    queryset = Ticket.objects.all()
