from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token
from accounts.models import User


class GoogleOAuthSerializer(serializers.Serializer):
    oauth_token = serializers.CharField(max_length=2550)
    username= serializers.CharField(max_length=250)
    phone_number = serializers.CharField(max_length=250)
    semester = serializers.CharField(max_length=250)
    batch = serializers.CharField(max_length=250)
    team = serializers.CharField(max_length=250)
    event_id = serializers.CharField(max_length=250)

    access_token = serializers.CharField(max_length=250, read_only=True)
    refresh_token = serializers.CharField(max_length=550, read_only=True)

    def validate(self, data):

        access_token = data.get('access_token')
        refresh_token = data.get('refresh_token')
        refresh = None

        client_id = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        idinfo = id_token.verify_oauth2_token(
            data.get('oauth_token'), requests.Request(), client_id)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        user = None

        # Using the information from google,
        # determine if an account exist of not
        try:
            user = User.objects.get(email=idinfo['email'])
        except Exception as exc:
            user = None

        if not user:
            try:
                user = User.objects.create_user_from_google(
                        email=idinfo['email'], username=data.get('username'))
            except Exception as exc:
                raise serializers.ValidationError("Error creation user for this account")

        try:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
        except Exception as exc:
            raise serializers.ValidationError(exc)

        try:
            from organizer.models import Event
            try:
                event = Event.objects.get(pk=data.get('event_id'))
                user.phone = data.get('phone_number')
                user.semester = data.get('semester')
                user.batch = data.get('batch')
                user.username = data.get('username')
                if (not event.closed):
                    user.save()
                else:
                    raise serializers.ValidationError("Event is closed")
            except Event.DoesNotExist:
                raise serializers.ValidationError("The event does not exist")

            if (event.team_based):
                event.teams = event.teams + "["+str(user.id)+","+data.get('team')+"]"
            event.attendees.add(user)
            if (not event.closed):
                event.save()
            else:
                raise serializers.ValidationError("Event is closed")
        except Exception as exc:
            raise serializers.ValidationError(exc)

        return {
            "oauth_token": "valid",
            "username": "valid",
            "team": "valid",
            "event_id": "valid",
            "phone_number": "valid",
            "semester": "valid",
            "batch": "valid",
            "access_token": access_token,
            "refresh_token": refresh_token
        }


class GoogleOAuthView(APIView):
    """ Google social authenticaion api """

    permission_classes = ()

    response = None
    response_code = None

    def post(self, request):
        """ post request handler which accepts a token """
        serializer = GoogleOAuthSerializer(data=request.data)
        if serializer.is_valid():
            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        return Response(self.response, self.response_code)
