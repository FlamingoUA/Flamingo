import json
import time

from django.http import HttpResponse
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework import permissions, filters
from rest_framework.pagination import PageNumberPagination
import requests

from model.models import Ticket
from .serializers import TicketSerializer

body_s = {
  "OTA_AirLowFareSearchRQ": {
    "OriginDestinationInformation": [
      {
        "DepartureDateTime": "2022-10-21T00:00:00",
        "DestinationLocation": {
          "LocationCode": "MIL"
        },
        "OriginLocation": {
          "LocationCode": "WAW"
        },
        "RPH": "0"
      }
    ],
    "POS": {
      "Source": [
        {
          "PseudoCityCode": "F9CE",
          "RequestorID": {
            "CompanyName": {
              "Code": "TN"
            },
            "ID": "1",
            "Type": "1"
          }
        }
      ]
    },
    "TPA_Extensions": {
      "IntelliSellTransaction": {
        "RequestType": {
          "Name": "200ITINS"
        }
      }
    },
    "TravelPreferences": {
      "TPA_Extensions": {
        "DataSources": {
          "ATPCO": "Enable",
          "LCC": "Disable",
          "NDC": "Disable"
        },
        "NumTrips": {}
      }
    },
    "TravelerInfoSummary": {
      "AirTravelerAvail": [
        {
          "PassengerTypeQuantity": [
            {
              "Code": "ADT",
              "Quantity": 1
            }
          ]
        }
      ],
      "SeatsRequested": [
        1
      ]
    },
    "Version": "3"
  }
}


def get_tickets(response, kwargs):
    token = ''
    if kwargs:
        token = kwargs['token']
    else:
        token = json.loads(response.body)['token']
    questionnaire_response = requests.post(
        url=f" https://api-crt.cert.havail.sabre.com/v3/offers/shop",
        data=json.dumps(body_s),
        params={
            'Authorization': f"Bearer {token}",
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }
    )
    response = json.loads(questionnaire_response.content)
    try:
        tickets = json.loads(questionnaire_response.content)['groupedItineraryResponse']['scheduleDescs']
    except KeyError:
        return HttpResponse('CRED ERROR')
    for ticket in tickets:
        try:
            price = response['groupedItineraryResponse']['taxSummaryDescs'][ticket['id'] - 1]['amount']
            currency = response['groupedItineraryResponse']['taxSummaryDescs'][ticket['id'] - 1]['currency']
        except IndexError:
            price = 0
            currency = ''
        Ticket.objects.create(
            name=(
                f"{ticket['departure']['city']}/{ticket['arrival']['city']}/"
                f"{ticket['departure']['time'][0]}"
            ),
            price=price,
            currency=currency,
            carrier=ticket['carrier']['operating'],
            flight_route=f"{ticket['departure']['city']} | {ticket['arrival']['city']}",
            departure_city=ticket['departure']['city'],
            departure_airport=ticket['departure']['airport'],
            departure_time=ticket['departure']['time'].split('+')[0],
            flight_route_time=time.strftime(
                "%H:%M:%S", time.gmtime(ticket['elapsedTime'])
            ),
            arrival_city=ticket['arrival']['city'],
            arrival_airport=ticket['arrival']['airport'],
            arrival_time=ticket['arrival']['time'].split('+')[0]
        )
    return HttpResponse(questionnaire_response)


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
