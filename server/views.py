from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import CustomUser, Task
from .serializers import UserSerializer, CustomUserSerializer
from .utils import generate_new_task



@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("Not found.", status=status.HTTP_404_NOT_FOUND)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})



@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    
    if serializer.is_valid():
        user = CustomUser(
            username=serializer.validated_data['username'],
        )
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token' : token.key, 'user' : serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_value(request):
    
    user = CustomUser.objects.get(username=request.data['username'])
    user.wins += request.data['wins']
    user.losses += request.data['losses']
    user.save()
    return Response(request.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def validate_answer(request):

    return redirect('check_task')
    


@api_view(['POST'])
def check_task(request):
    
    print(request)

    auth_header = request.META.get('HTTP_AUTHORIZATION')

    if auth_header:
        try:
            token = auth_header.split()[1]
            token = Token.objects.get(key=token)
            user = token.user

            print("poszlo")
            return JsonResponse(request.data, status=status.HTTP_200_OK)
        except Exception as error:

            return JsonResponse(error, status=status.HTTP_404_NOT_FOUND)


    return Response(status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def generate_task(request):

    data = generate_new_task()

    answer = "".join(data["answer"])

    task = Task.objects.create(correct_answer=answer, is_completed=False)

    task.save()

    data["task_id"] = task.task_id

    return JsonResponse(data, status=200)



