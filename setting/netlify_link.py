import os
import requests

slack_webhook = os.environ.get('CLIENT_SLACK')
link = os.environ.get('deployment')

payload = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"<{link}/report.html|Link Report Test>"
            }
        }
    ]
}
header = {"content-type": "application/x-www-form-urlencoded"}
requests.post(slack_webhook, json=payload, headers=header)
