from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
