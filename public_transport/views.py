from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import PublicTransport
from .serializers import PublicTransportSerializer
from rest_framework.response import Response

class PublicTransportAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        transports = PublicTransport.objects.all()
        serializer = PublicTransportSerializer(transports, many=True)
        return Response(serializer.data)