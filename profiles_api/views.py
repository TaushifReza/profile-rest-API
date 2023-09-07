from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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


class HellowViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request):
        """Return Hello message"""
        a_viewset = [
            "User action (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provide more funcationality with less code",
        ]
        return Response(
            {
                "message": "Hello!",
                "a_viewset": a_viewset,
            }
        )

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({"http_method": "DELETE"})
