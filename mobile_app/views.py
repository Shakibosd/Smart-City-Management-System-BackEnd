from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import MobileAppFeature
from .serializers import MobileAppFeatureSerializer

class MobileAppFeatureView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        features = MobileAppFeature.objects.all()
        serializer = MobileAppFeatureSerializer(features, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileAppFeatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
