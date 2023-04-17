import requests
from setting.general import *


def webhook_slack(color, success, failed, all, success_rate):
    sr = round(success_rate, 2)

    if slack_title is None:
        title = "Reports Automation Api"
    else:
        title = str(slack_title)

    param = {
        "attachments": [
            {
                "color": str(color),
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Haloo",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Success Test:*\n 10"
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Failed Test:*\n 5"
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
                                "text": "*Total Test:*\n 15"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Success Rate:*\n 10%"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<https://google.com|Check Detail Report>"
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
