from django.shortcuts import render
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from django.shortcuts import get_list_or_404, get_object_or_404
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
# from paypal.standard.forms import PayPalPaymentsForm

class OrderViewSet(viewsets.ModelViewSet):

    """
    order details
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url':'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    #return render(request, 'ecommerce_app/process_payment.html', {'order': order, 'form': form})
    data = {'order': order, 'form': form}
    return Response(data)


@csrf_exempt
def payment_done(request):
    return Response(request, 'payment done')


@csrf_exempt
def payment_canceled(request):
    return Response(request, 'payment_cancelled')
