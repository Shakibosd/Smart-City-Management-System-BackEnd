from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DeshboardAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        data = {
            "trafic status" : "Normal",
            "public safty status" : "Secure",
            "public transport status" : "Operational"
        }
        return Response(data)