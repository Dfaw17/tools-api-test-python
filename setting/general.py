# POSTKU
import os

username_postku = "admin1"
pwd_postku = "admin1"
username_postku_not_found = "admin170901"

# GENERAL
max_latency = 1000000

# TEST CASE MANAGEMENT
api_key = "8b8d6169357d45082a3c818240449a38b7a56fddafdfe3aa0bdda8a32c5bf632"
host_test_management = "https://api.qase.io/v1/result"
test_run = 8
test_code_project = "TF"

# SLACK NOTIFICATION
slack_webhook = os.environ.get('SLACK_NOTIF')
FAWWAZ = os.environ.get('FAWWAZ')
slack_title = os.environ.get('TEST')
url_artifact = os.environ.get('RUNID')
notif_slack = "ON"
notif_slack_just_failed = "NO"