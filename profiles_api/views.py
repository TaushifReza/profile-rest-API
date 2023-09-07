from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request, formate=None):
        """Return list of a APIView features"""
        an_apiview = [
            "Uses HTTP methos as a function(get, post, patch, put, delete)",
            "Is similare to traditional Django View",
            "Give most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response(
            {
                "messages": "Hello!",
                "an_apiview": an_apiview,
            }
        )

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an Object"""
        return Response({"message": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial updating an Object"""
        return Response({"message": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({"message": "DELETE"})
