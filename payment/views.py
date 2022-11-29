from django.shortcuts import render
from payment.models import Billing
from payment.serializers import BillingSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import json
import base64


class BillingViewSet(viewsets.ModelViewSet):
    """
    payment details of the order
    """
    
    serializer_class = BillingSerializer
    queryset = Billing.objects.all()



@api_view(['POST'])
def PaypalToken(client_ID, client_Secret):

    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    data = {
                "client_id":client_ID,
                "client_secret":client_Secret,
                "grant_type":"client_credentials"
            }
    headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic {0}".format(base64.b64encode((client_ID + ":" + client_Secret).encode()).decode())
            }

    token = requests.post(url, data, headers=headers)
    return token.json()['access_token']