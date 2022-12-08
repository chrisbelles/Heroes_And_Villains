from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.serializers import SuperTypeSerializer
from super_types.models import SuperType

# Create your views here.

@api_view(['GET', 'POST'])
def superType_list(request):
    if request.method == 'GET':
        super_name = request.query_params.get('super')
        print(super_name)
        supers = SuperType.objects.all()
        if super_name:
            supers = supers.filter(super__name=super_name)
        serializer = SuperTypeSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def superType_detail(request, pk):
    superType = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(superType)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(superType, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        superType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)