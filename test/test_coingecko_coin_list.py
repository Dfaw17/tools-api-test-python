import pytest
import requests
from assertpy import assert_that
import setting.endpoint as url
import setting.general as general
from json_schema.schema_response_coingecko import *
from jsonschema import validate as validate_json_schema


@pytest.mark.TestManagement(3)
def test_coin_list_normal():
    req = requests.get(url.coingecko_coin_list)

    # VERIFY
    verify_status_code = req.status_code
    verify_latency = req.elapsed.microseconds
    verify_resp_key = req.json()[0]

    # ASSERT
    assert_that(verify_status_code).is_equal_to(200)
    assert_that(verify_resp_key).contains_key('id', 'symbol', 'name')
    assert_that(verify_latency).is_less_than(general.max_latency)
    validate_json_schema(instance=req.json(), schema=coin_list_normal)
