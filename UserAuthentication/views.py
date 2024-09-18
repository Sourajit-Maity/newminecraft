from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# REST API interface with authentication
# ----------------------------------------------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from datetime import datetime
from DataExtractor import defaults

RET_DATA = 'data'
RET_STATUS = 'status'
RET_MSG = 'msg'

# Create your views here.

# ======================================================================
# Login/logout - START
# ======================================================================
@api_view(["POST"])
@permission_classes((AllowAny,))
@csrf_exempt
def login(request):
    try:
        email = request.data.get("email")
        password = request.data.get("password")
        defaults.logger("login: entered", [email, password], level="info")
        if email is None or password is None:
            return Response({RET_STATUS: False, RET_MSG: 'Please provide both email and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=email, password=password)

        if not user:
            defaults.logger("Login failed", email, level="debug")
            return Response({RET_STATUS: False, RET_MSG: 'Invalid Credentials'}, status=HTTP_200_OK)

        defaults.logger("Login", user.id, level="debug")

        t_user = User.objects.get(id = user.id)
        t_user.last_login = datetime.now()
        t_user.save()
        

        token, _ = Token.objects.get_or_create(user=user)
        defaults.logger("Login success", str(token.key), level="debug")

        # --------------------------------------------------------

        return Response({
            RET_STATUS: True,
            RET_MSG: "Login success",
            'username': user.email.split('@')[0],
            'email': user.email,
            'token': token.key,
        }, status=HTTP_200_OK)
    except Exception as e:
        defaults.logger("Login Exception:", e, level="error")
        return Response({RET_STATUS: False, RET_MSG: str(e)}, status=HTTP_400_BAD_REQUEST)
# ======================================================================


@api_view(["GET"])
def logout(request):
    """simply delete the token to force a login"""
    request.user.auth_token.delete()
    data = {
        RET_STATUS: True,
        RET_MSG: 'Successfully logged out'
    }
    return Response(data=data, status=HTTP_200_OK)

# ======================================================================
# Login/logout - END
# ======================================================================

# ======================================================================
# Auth Screen Views
# ======================================================================

def login_view(request):
	return render(request, 'auth/login.html')

# ======================================================================




