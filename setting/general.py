# POSTKU
import os

username_postku = ""
pwd_postku = ""
username_postku_not_found = "admin170901"

# GENERAL
max_latency = 1000000

# TEST CASE MANAGEMENT
api_key = ""
host_test_management = "https://api.qase.io/v1/result"
test_run = 8
test_code_project = "TF"

# SLACK NOTIFICATION
slack_webhook = ""
slack_title = os.environ.get('TEST')
url_artifact = os.environ.get('RUNID')
notif_slack = "ON"
notif_slack_just_failed = "NO"
