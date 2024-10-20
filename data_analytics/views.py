from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import AnalyticsData
from .serializers import AnalyticsDataSerializer

class AnalyticsDataView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        analytics = AnalyticsData.objects.all()
        serializer = AnalyticsDataSerializer(analytics, many=True)
        return Response(serializer.data)
