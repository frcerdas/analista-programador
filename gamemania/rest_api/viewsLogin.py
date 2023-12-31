from django.shorcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data =JSONParser().parse(request)
    username=data['username']
    password=data['password']

try:
    user = user.objects.get(username=username)
    except User.DoesNotExist