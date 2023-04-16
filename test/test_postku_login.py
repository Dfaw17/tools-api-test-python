import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_postku import *
from jsonschema import validate as validate_json_schema
from setting.general import *


@pytest.mark.TestManagement(7)
def test_login_normal():
    payload = {
        "username": username_postku,
        "pwd": pwd_postku
    }
    req = requests.post(url.postku_login, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_msg = req.json().get("msg")
    verify_token = req.json().get("token")["access_token"]

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_msg).is_equal_to("Success login account")
    assert_that(verify_token).is_not_none()
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=login_normal)


@pytest.mark.TestManagement(8)
def test_login_acc_not_found():
    payload = {
        "username": username_postku_not_found,
        "pwd": pwd_postku
    }
    req = requests.post(url.postku_login, json=payload)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_msg = req.json().get("msg")
    verify_token = req.json().get("token")["access_token"]

    # ASSERT
    assert_that(verify_status_code).is_equal_to(404)
    assert_that(verify_msg).is_equal_to("Invalid: account not found")
    assert_that(verify_token).is_none()
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=login_error)
