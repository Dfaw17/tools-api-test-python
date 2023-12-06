# POSTKU
import os

username_postku = "admin1"
pwd_postku = "admin1"
username_postku_not_found = "admin170901"

# GENERAL
max_latency = 1000000

# TEST CASE MANAGEMENT
api_key = os.environ.get('API_KEY_QASE')
host_test_management = "https://api.qase.io/v1/result"
test_run = 9
test_code_project = "TF"

# SLACK NOTIFICATION
slack_webhook = "https://hooks.slack.com/services/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"
slack_title = os.environ.get('TEST')
url_artifact = os.environ.get('RUNID')
notif_slack = "OFF"
notif_slack_just_failed = "NO"
