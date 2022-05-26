from rest_framework import serializers
from .models import Book
#from core.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    #genre = serializers.CharField(source='get_genre_display')
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

        extra_kwargs = {
            "id": {"read_only": True},
            "uuid": {"read_only": True},
            "status": {"read_only": True},
            "library": {"read_only": True}
        }
