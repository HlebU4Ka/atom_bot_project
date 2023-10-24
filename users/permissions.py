from rest_framework import permissions
from rest_framework.views import APIView


class YourView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]