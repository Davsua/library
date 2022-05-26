from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
# Create your views here.
from .serializers import UserSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from place.models import Book
from place.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    @action(detail=True)
    def my_books(self, request,  pk=None):
        queryset = Book.objects.filter(
            booktenant__id=pk
        )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def my_books_on_rented(self, request,  pk=None):
        queryset = Book.objects.filter(
            booktenant__id=pk
        ).values_list("booktenant__id", flat=True)
        book = Book.objects.filter(
            id__in=queryset
        )
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    