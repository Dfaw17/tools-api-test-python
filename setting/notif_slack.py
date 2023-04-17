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
                "color": color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": title,
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n{success}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n{failed}"
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
                                "text": f"*Total Test:*\n{all}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Rate:*\n{sr}%"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<{url_artifact}|Check Detail Report>"
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
