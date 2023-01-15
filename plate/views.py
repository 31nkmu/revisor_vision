import json

from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from plate.models import Plate
from plate.serializers import PlateSerializer
from plate.services import generate_plate


class GeneratePlateApiView(ListAPIView):
    def get(self, request):
        amount = request.data.get('amount', 1)
        res = []
        for i in range(int(amount)):
            plate = generate_plate()
            while Plate.objects.filter(plate=plate).exists():
                plate = generate_plate()
            res.append(plate)
        data = json.dumps(res, ensure_ascii=False)
        return Response(data, status=status.HTTP_200_OK)
    permission_classes = (IsAuthenticated,)


class ListPlateApiView(ListAPIView):
    def get(self, request):
        id_ = request.data.get('uuid')
        if not id_:
            return Response('введите uuid поле')
        data = Plate.objects.filter(uuid=id_)
        if not data.exists():
            return Response('нет номера под таким uuid')
        serializer = PlateSerializer(data[0], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    permission_classes = (IsAuthenticated,)


class AddPlateApiView(CreateAPIView):
    queryset = Plate
    serializer_class = PlateSerializer
    permission_classes = (IsAuthenticated,)
