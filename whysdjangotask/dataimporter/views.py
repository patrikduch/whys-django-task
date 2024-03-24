from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DynamicModel
from .serializers import DynamicModelSerializer

@api_view(['POST'])
def import_data(request):
    if request.method == 'POST':
        serializer = DynamicModelSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_model_list(request, model_name):
    models = DynamicModel.objects.filter(name=model_name)
    serializer = DynamicModelSerializer(models, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail_model_data(request, model_name, pk):
    model = get_object_or_404(DynamicModel, name=model_name, pk=pk)
    serializer = DynamicModelSerializer(model)
    return Response(serializer.data)