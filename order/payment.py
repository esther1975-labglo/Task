import stripe
import json
from django.conf import settings
from rest_framework import (
    permissions, response, status, views
)
from payment.models import Billing
from order.models import Order
from payment.utils import payment_confirmation, send_confirmation_mail

stripe.api_key = settings.SECRET_KEY


class GetPublishableKey(views.APIView):

    def get(self, request):
    	return response.Response(
            data={"publishable_key": settings.PUBLISHABLE_KEY},
        )

class GetCheckoutSession(views.APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
       
        id = request.GET.get('sessionId', '').strip()
        if not id:
            return response.Response(
                {'error': 'Please provide a valid session id'},
                status=status.HTTP_400_BAD_REQUEST
            )
        checkout_session = stripe.checkout.Session.retrieve(id)
        return response.Response(
            data={'checkout_session': checkout_session}
        )

class CreateCheckoutSession(views.APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            print('checkout_session response', request.data)

            user = request.data["user"]
           

            domain_url = 'http://' + request.get_host().split(':')[0].lower()
            user = Order.objects.get(id=user)
            
            registration_id = user.id
            registration_id = str(registration_id)
            
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url,
                cancel_url=domain_url,
                payment_method_types=['card'],
                mode='payment',
                user=User.id,
                # automatic_tax={'enabled': True},
                line_items=[
                    {
                    
                    'currency': 'usd',
                    'amount': int(100),
                    'quantity': 1,
                    }
                ]
            )

            stripe_response_data = json.dumps(checkout_session)
            stripe_transaction_id = checkout_session['id']
            stripe_status = checkout_session['status']

            Payment.objects.create(
                stripe_token=checkout_session["payment_intent"],
                stripe_transaction_id=stripe_transaction_id,
                stripe_status=stripe_status, stripe_response_data=stripe_response_data
            )
            return response.Response(
                {"sessionId": checkout_session["id"]},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return response.Response(
                {"error": str(e)}, status=status.HTTP_400_BAD_REQUEST
            )

