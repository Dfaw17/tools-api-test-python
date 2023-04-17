import requests
from setting.general import *


def test_debug():
    payload = {"text": "Hello pycharm"}
    req = requests.post(slack_webhook, json=payload)
