import os
import json
import logging
import time
from pythonjsonlogger import jsonlogger
from dotenv import load_dotenv

logger = logging.getLogger()
logHandler = logging.FileHandler(filename='whoop-logs.json')
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)


load_dotenv()

username = os.getenv("USERNAME") or ""
password = os.getenv("PASSWORD") or ""

def print_pretty(my_dict):
    output = json.dumps(my_dict)
    print(output)

from whoop import WhoopClient

client = WhoopClient(username, password)

client.authenticate()

profile = client.get_profile()
body = client.get_body_measurement()
sleeps = client.get_sleep_collection()
recoveries = client.get_recovery_collection()

while True:

    cycles = client.get_cycle_collection()
    print("***** MOST RECENT WHOOP DATA *****")
    print("--- PROFILE ---")
    print(profile)
    print()
    logger.info(profile)

    print("--- BODY MEASUREMENTS ---")
    print(body)
    print()
    logger.info(body)

    print("--- SLEEP ----")
    print(sleeps[0])
    print()
    logger.info(sleeps[0])

    print("--- RECOVERY ---")
    print(recoveries[0])
    print()
    logger.info(recoveries[0])

    print("--- CYCLE ---")
    print(cycles[0])
    print()
    logger.info(cycles[0])
    
    time.sleep(30)
    
""" 
API LOGGING 
"""
"""
Send deflate logs returns "Request accepted for processing (always 202 empty JSON)." response
"""

# from datadog_api_client import ApiClient, Configuration
# from datadog_api_client.v2.api.logs_api import LogsApi
# from datadog_api_client.v2.model.content_encoding import ContentEncoding
# from datadog_api_client.v2.model.http_log import HTTPLog
# from datadog_api_client.v2.model.http_log_item import HTTPLogItem

# body = HTTPLog(
#     [
#         HTTPLogItem(
#             ddsource="python",
#             ddtags="env:dev",
#             message=str(cycles[0]),
#             service="whoop",
#         ),
#     ]
# )

# configuration = Configuration()
# with ApiClient(configuration) as api_client:
#     api_instance = LogsApi(api_client)
#     response = api_instance.submit_log(content_encoding=ContentEncoding.DEFLATE, body=body)

#     print(response)
