import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_coingecko import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(4)
def test_ping_server_normal():
    req = requests.get(url.coingecko_ping_server)

    # VERIFY
    verify_status_code = req.status_code
    verify_message = req.json().get("gecko_says")
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_message).is_equal_to("(V3) To the Moon!")
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=ping_server_normal)


@pytest.mark.TestManagement(5)
def test_ping_server_invalid_url():
    req = requests.get(url.coingecko_ping_server + 's')

    # VERIFY
    verify_status_code = req.status_code
    verify_message = req.json().get("error")
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(404)
    assert_that(verify_message).is_equal_to("Incorrect path. Please check https://www.coingecko.com/api/")
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=ping_server_error)


@pytest.mark.TestManagement(6)
def test_ping_server_invalid_methode():
    req = requests.delete(url.coingecko_ping_server)

    # VERIFY
    verify_status_code = req.status_code
    verify_message = req.json().get("error")
    verify_latency = req.elapsed.microseconds

    # ASSERT
    assert_that(verify_status_code).is_equal_to(404)
    assert_that(verify_message).is_equal_to("Incorrect path. Please check https://www.coingecko.com/api/")
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=ping_server_error)
