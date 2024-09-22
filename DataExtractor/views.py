from django.shortcuts import render

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
import shutil
import os
import io
import pandas as pd
from datetime import datetime
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from . import defaults
from .models import *

RET_DATA = 'data'
RET_STATUS = 'status'
RET_MSG = 'msg'
base_dir = os.path.dirname(os.path.dirname(__file__))

# Create your views here.

# ======================================================================
# Home Screen Views
# ======================================================================

def home_view(request):
	return render(request, 'home/index.html')

# ======================================================================


# ======================================================================
# Data Converter - START
# ======================================================================    

@api_view(["POST"])
def upload_master_file(request):
    try:
        entered_info = defaults.get_entered_info(request)
        defaults.logger("upload_master_file: Entered", entered_info, level="info")

        upload_file = entered_info.get('ProductFile')
        content = upload_file.read()
        upload_file_name = upload_file.name
        
        if content is not None:
            feedback_df =  pd.io.excel.read_excel(io.BytesIO(content))
            # print(feedback_df)

            feedback_df = feedback_df[['user', 'time', 'x', 'y', 'z']]

            model_instance = [feedback(**data) for index, data in feedback_df.iterrows()]
            feedback.objects.bulk_create(model_instance)
    
            return Response({
                RET_STATUS: True,
                RET_DATA: upload_file_name,
                RET_MSG: "Master file uploaded successfully !!!",
            }, status=HTTP_200_OK)
        
        else:
            return Response({
                RET_STATUS: False,
                RET_MSG: "Uploaded file doesn't have any content!!!",
            }, status=HTTP_200_OK)
        
    except Exception as e:
        defaults.logger("upload_master_product_file Exception: ", e, level="error")
        return Response({RET_STATUS: False, RET_MSG: str(e)}, status=HTTP_400_BAD_REQUEST)
    
# ======================================================================
@api_view(["GET"])
def get_feedback_data(request):
    try:
        entered_info = defaults.get_entered_info(request)
        defaults.logger("get_feedback_data: Entered", entered_info, level="info")

        # upload_file = entered_info.get('ProductFile')

        data = feedback.objects.all().values()

        return Response({
            RET_STATUS: True,
            RET_DATA: data,
        }, status=HTTP_200_OK)

        
    except Exception as e:
        defaults.logger("get_feedback_data Exception: ", e, level="error")
        return Response({RET_STATUS: False, RET_MSG: str(e)}, status=HTTP_400_BAD_REQUEST)
     
# ======================================================================
# Data Converter - END
# ======================================================================
