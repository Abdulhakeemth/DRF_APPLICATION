from django.shortcuts import render
from rest_framework import status
from application.serializers import DictionarySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dictionary
from functools import wraps
from rest_framework.permissions import IsAuthenticated
class DictionaryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        dictionary = Dictionary.published.all()
        serializer = DictionarySerializer(dictionary, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
def resource_checker(model):
    def check_entity(fun):
        @wraps(fun)
        def inner_fun(*args, **kwargs):
            try:
                x = fun(*args, **kwargs)
                return x
            except model.DoesNotExist:
                return Response({'message': 'Not Found'}, status=status.HTTP_204_NO_CONTENT)
        return inner_fun
    return check_entity
  
   
    
class DictionaryDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    @resource_checker(Dictionary)
    def get(self, request, pk, format=None):
        dictionary = dictionary.published.get(pk=pk)
        serializer = DictionarySerializer(dictionary)
        return Response(serializer.data)

    @resource_checker(Dictionary)
    def get(self,request,pk,format=None):
        search= Dictionary.objects.filter(pk=pk)
        serializer = DictionarySerializer(search,many=True)
        return Response(serializer.data)    

    @resource_checker(Dictionary)
    def put(self, request, pk, format=None):
        dictionary = Dictionary.published.get(pk=pk)
        serializer = DictionarySerializer(dictionary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @resource_checker(Dictionary)
    def delete(self, request, pk, format=None):
        dictionary = Dictionary.published.get(pk=pk)
        dictionary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
