from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home_view(request):
    return HttpResponse("Welcome to the Study Cards API!")

@api_view(['GET'])
def test_connection(request):
    return Response({"message": "Connection is successful!"})

