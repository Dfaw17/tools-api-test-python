import requests

import setting.general as data


def webhook_slack(color, success, failed, all, success_rate):
    sr = round(success_rate, 2)

    if data.slack_title is None:
        slack_title = "Reports Automation Api"
    else:
        slack_title = str(data.slack_title)

    param = {
        "attachments": [
            {
                "color": color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": slack_title,
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
                            "text": f"<{data.url_artifact}|Check Detail Report>"
                        }
                    }
                ]
            }
        ]
    }

    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    print("\nDEBUG : " + str(data.slack_webhook))
    if data.notif_slack == "ON":
        print("\nHOLAAA")
        requests.post(data.slack_webhook, json=param, headers=header)
    else:
        print("NOTIF OFF")
