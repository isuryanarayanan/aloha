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
    description =serializers.CharField(trim_whitespace=False)
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

@api_view(['GET'])
def EventAdminDetailView(request, pk):
    try: 
        event = Event.objects.get(pk=pk) 
    except Event.DoesNotExist: 
        return JsonResponse({'message': 'The Event does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        event_serializer = EventSerializer(event)
        attends = []
        teams = []


        if(event.team_based and len(event.teams)>1):
            for i in event.teams.split(',]['):
                i = i.replace("]","")
                i= i.replace("[","")
                i = i.split(",")
                i = [x for x in i if x != ""]
                teams = teams+[i]
            for team in teams:
                team_user = User.objects.get(id=team[0])
                attends = attends+[{"id":team_user.id,"email":team_user.email,"phone":team_user.phone,"semester":team_user.semester,"batch":team_user.batch,"name":team_user.username,"team":team} ]
        else:
            for i in event_serializer.data['attendees']:
                user =User.objects.get(id=i)
                attends = attends+[{"id":user.id,"email":user.email,"phone":user.phone,"semester": user.semester,"batch":user.batch,"name":user.username,"team":0} ]


        return Response(attends,200)

 
