import pytest
from setting.case_management import *


def pytest_html_report_title(report):
    report.title = "Report API Automation"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    get_error = request.session.testsfailed

    yield

    test_result = request.session.testsfailed - get_error
    marker = request.node.get_closest_marker("TestManagement")

    if marker is None:
        print("there is test case id")
    else:
        if test_result == 0:
            case_management_push_result(str(marker.args[0]), "passed")
        else:
            case_management_push_result(str(marker.args[0]), "failed")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # print("\nbefore suite")

    yield

    # print("after suite")
    test_success = len(request.session.items) - request.session.testsfailed
    test_failed = request.session.testsfailed
    test_all = len(request.session.items)
    success_rate = test_success / test_all * 100

    if test_failed > 0:
        color = "FF1E00"
    else:
        color = "2B7A0B"

    # webhook_slack(color, test_success, test_failed, test_all, success_rate)
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
                                "text": f"*Success Test:*\n{test_success}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n{test_failed}"
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
                                "text": f"*Total Test:*\n{test_all}"
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
