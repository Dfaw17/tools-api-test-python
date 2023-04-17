import requests
from setting.general import *


def webhook_slack(color, success, failed, all, success_rate):
    sr = round(success_rate, 2)

    param = {
        "attachments": [
            {
                "color": str(color),
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Test Automation Report",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n {success}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n {failed}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Skipped Test:*\n0"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Total Test:*\n {all}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Rate:*\n {sr}%"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<https:/dfaw17.github.io|Check Detail Report>"
                        }
                    }
                ]
            }
        ]
    }

    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    requests.post(slack_webhook, json=param, headers=header)


def webhook_debug():
    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    param = {"text": "Hello faw"}
    requests.post(slack_webhook, json=param, headers=header)
