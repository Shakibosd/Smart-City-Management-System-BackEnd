from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
# from sslcommerz_lib import SSLCOMMERZ
from .models import Payment
# from .serializers import PaymentSerializer
from rest_framework import status

class PaymentInitiateAPIView(APIView):
    def post(self, request):
        # SSLCommerz configuration
        settings = {
            'store_id': 'your_store_id',
            'store_pass': 'your_store_password',
            'issandbox': True  # Make it False in production
        }
        # sslcz = SSLCOMMERZ(settings)
        
        post_body = {}
        post_body['total_amount'] = request.data.get('amount')
        post_body['currency'] = "BDT"
        post_body['tran_id'] = "TRAN_" + str(request.user.id)
        post_body['success_url'] = 'http://yourdomain.com/payment/success/'
        post_body['fail_url'] = 'http://yourdomain.com/payment/fail/'
        post_body['cancel_url'] = 'http://yourdomain.com/payment/cancel/'
        post_body['cus_name'] = request.user.username
        post_body['cus_email'] = request.user.email
        post_body['cus_phone'] = request.data.get('phone')

        # response = sslcz.createSession(post_body)

        # if 'GatewayPageURL' in response:
        #     # Save the payment object
        #     payment = Payment.objects.create(
        #         user=request.user,
        #         transaction_id=post_body['tran_id'],
        #         amount=request.data.get('amount'),
        #     )
        #     # return Response({'GatewayPageURL': response['GatewayPageURL']}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'error': 'Unable to initiate payment'}, status=status.HTTP_400_BAD_REQUEST)


class PaymentSuccessAPIView(APIView):
    def post(self, request):
        tran_id = request.data.get('tran_id')
        status = request.data.get('status')

        try:
            payment = Payment.objects.get(transaction_id=tran_id)
            if status == "VALID":
                payment.status = "Completed"
                payment.save()
                return Response({'message': 'Payment successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Payment failed'}, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({'message': 'Invalid transaction ID'}, status=status.HTTP_404_NOT_FOUND)
