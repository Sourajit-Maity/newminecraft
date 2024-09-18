import logging
from django.conf import settings
from django.db import connections

from rest_framework.response import Response
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

# Set the log level
LOG_LEVEL = "DEBUG"

# Set the logger settings
logging.basicConfig(format='%(asctime)s-%(levelname)-6s[(%(threadName)-10s)]:%(message)s', datefmt='%d-%b-%y %H:%M:%S', level=LOG_LEVEL, 
                    handlers=[logging.FileHandler('BEVCO_data_extractor.log'), logging.StreamHandler()])


LENGTH_SMALL = 25
LENGTH_BIG = 50
LENGTH_LARGE = 100
LENGTH_EX_LARGE = 255 
# ======================================================================
# Utility functions
# ======================================================================
def get_entered_info(request):
	#Defaults.logger("get_entered_info():"+request.method, level="info")
	entered_info = None
	try:
		if request.method == 'POST':
			entered_info = request.data  # Passed as body
		else:
			entered_info = request.query_params.dict()

	except Exception as e:
		logger(
			"get_entered_info(): No entered info found!", e, level="error")
	return entered_info

# ======================================================================

# ================ Logger Functions ==================
# imports required to add calling functions filename+line number
from inspect import getframeinfo, stack
import os
import sys
import traceback


# Logging method
def logger(tag = "", value = "", level = "info"):
    # add calling functions filename+line number
    caller = getframeinfo(stack()[1][0])
    only_filename = os.path.basename(caller.filename)
    caller_str = "%-18s:%-3d|" % (only_filename, caller.lineno)
    tag = "|"+caller_str+tag

    if level == "debug":
        logging.debug("= %s = %s", tag, value)
        
    elif level == "info":
        logging.debug(" INFO = %s = %s", tag, value)
        #logging.info("= %s", tag+"["+str(value)+"]")
        
    elif level == "warning":
        logging.debug("= %s = %s", tag, value)
        
    elif level == "error":
        if isinstance(value, Exception):
            # logging.exception("\n\t!!!!!!! = %s = %s", tag, value, exc_info=1)
            # print(traceback.print_exc(limit=1, file=sys.stdout))
            logging.exception('\n\t!!!!!!! = {} = {}'.format(tag, value))
        else:
            # logging.error("\n\t!!!!!!! = %s = %s", tag, value)
            # print(traceback.print_exc(limit=1, file=sys.stdout))
            logging.exception('\n\t!!!!!!! = {} = {}'.format(tag, value))
    else:
        print("!!!UNKNOWN LOGGING LEVEL!!!"+level+" FROM "+ caller_str)
# =============================================================================

# ================ Response Functions ==================
RET_STATUS = 'status'
RET_MSG = 'msg'

def dataResponse(data=None, ret_msg = "OK", ret_status = True, status = HTTP_200_OK):   #Use this function to retuen data response
    response_data = {
        'data'      :   data,
        RET_MSG     :   ret_msg, 
        RET_STATUS  :   ret_status,
    }
    return Response(response_data, status=status)

def errorResponse(fn_name, error, errorCause=None):      #Use this function to return error response
    errorCause_prn = "" if errorCause is None else errorCause

    fn_name_delim = ":"
    if error is None:
        logger(fn_name, errorCause_prn, level="debug")
    elif isinstance(error, Exception):
        fn_name_delim = " Exception!! "
        logger(fn_name+fn_name_delim+str(errorCause_prn), error, level="error")
    else:
        logger(fn_name+":"+str(error), errorCause_prn, level="debug")

    error_resp = {
        RET_STATUS : False,
        'error_cause' : str(error) if errorCause is None else str(errorCause),
        RET_MSG    : "Internal error - "+fn_name+fn_name_delim+str(error),
    }
    return Response(error_resp, status=HTTP_500_INTERNAL_SERVER_ERROR)

# =============================================================================