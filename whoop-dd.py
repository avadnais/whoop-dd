import os
import json
import logging
from dotenv import load_dotenv

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
cycles = client.get_cycle_collection()

print(profile)
print(body)
# for cycle in cycles:
#     print_pretty(cycle)

print(cycles[0])
