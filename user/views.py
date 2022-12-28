from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from user.models import User
from rest_framework.authtoken.models import Token
from user.serializers import CreateUserSerializer, LoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_customer(request):
    """
    customer registration
    """
    return create_user(request, True)
    #return Response(request, create_user, False)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_restaurant(request):
    """
    restaurant registration
    """
    return create_user(request, True)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    token generation of registered user
    """

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


class LoginView(APIView):
    """
    user login 
    """

    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'})
        login(request, user)
        token, li = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})