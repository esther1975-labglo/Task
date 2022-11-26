from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from user.models import User
from user.serializers import CreateUserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_customer(request):
    return create_user(request, False)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_restaurant(request):
    return create_user(request, True)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    user = User.objects.filter(
        username__exact=request.data['username']).first()
    if user is None:
        return Response({'message': 'unauthorized'}, status=401)
    r = requests.post(
        BASE_URL + 'token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
           
        },
    )

    res = r.json()
    user = User.objects.filter(
        username__exact=request.data['username']).first()
    res['user_role'] = 'restaurant' if user.is_restaurant else 'customer'

    return Response(res, status=r.status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    
    r = requests.post(
        BASE_URL + 'token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
          
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    data = requests.post(
        BASE_URL + 'revoke_token/',
        data={
            'token': request.data['token'],
          },
    )
    if data.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, data.status_code)
   
    return Response(data.json(), data.status_code)


def create_user(request, is_restaurant):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            email=request.data['email'], is_restaurant=is_restaurant)
        data = requests.post(
            BASE_URL + 'token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                
            },
        )
        res = data.json()
        res['user_role'] = 'restaurant'
        return Response(res)
    return Response(serializer.errors)
