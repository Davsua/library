from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.models import User
from core.serializers import UserSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True)
    def my_books(self, request, pk=None):
        queryset = User.objects.filter(
            email__id=pk,
            email=pk
        )
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
