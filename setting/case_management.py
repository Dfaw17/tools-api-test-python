import requests
from setting.general import *


def case_management_push_result(test_case, status):
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Token": api_key
    }
    payload = {
        "case_id": test_case,
        "status": status
    }
    url = f"{host_test_management}/{test_code_project}/{test_run}"
    req = requests.post(url, json=payload, headers=headers)
