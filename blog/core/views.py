from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .models import Member
from .serializers import MemberSerializer, MemberSimpleSerializer

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Member.objects.all()
        serializer = MemberSimpleSerializer(queryset, many=True)

        return Response(serializer.data)
