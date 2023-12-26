from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from account.models.account import User


def signup(username: str, password: str):
    """
    Signup checks for user existence and returns User object 
    """
    existing_user = User.objects.filter(username=username, is_active=True).exists()
    if existing_user:
        return Response(
            {'detail': 'user already exists. proceed to login.'}, 
            status=status.HTTP_400_BAD_REQUEST
            )
    try:
        user = create_user(username=username, password=password)
    except Exception as e:
        return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    return Response(
        {'message': 'Successfully registered.', 'token': token.key}, 
        status=status.HTTP_201_CREATED
        )


def create_user(username: str, password=None):
    user = User.objects.create(
        username=username,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.is_active = True
        user.set_password(password)
        user.save()
    return user
