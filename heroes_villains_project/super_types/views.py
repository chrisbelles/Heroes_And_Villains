from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.serializers import SuperTypeSerializer
from super_types.models import SuperType

# Create your views here.

@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        dealership_name = request.query_params.get('dealership')
        print(dealership_name)
        cars = SuperType.objects.all()
        if dealership_name:
            cars = cars.filter(dealership__name=dealership_name)
        serializer = SuperTypeSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)