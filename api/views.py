from rest_framework import viewsets
from houses.models import House
from .serializers import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
