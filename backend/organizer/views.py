from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from organizer.models import Event
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

@api_view(['GET'])
def EventDetailView(request, pk):
    try: 
        event = Event.objects.get(pk=pk) 
    except Event.DoesNotExist: 
        return JsonResponse({'message': 'The Event does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        event_serializer =EventSerializer(event) 
        return Response(event_serializer.data)

@api_view(['GET'])
def EventView(request):
    mes = Event.objects.all()
    serializer =EventSerializer(mes, many=True)  # convert into JSON
    return Response(serializer.data)

@api_view(['POST'])
def RegisterEvent(request, pk):
    try: 
        event = Event.objects.get(pk=pk) 
    except Event.DoesNotExist: 
        return JsonResponse({'message': 'The Event does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        event_serializer =EventSerializer(event) 
        return Response(event_serializer.data)

 
