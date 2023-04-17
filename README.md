# Tools API Testing Python



this is e2e framework api test, has integrated with slack for notification, test management, netlify, and github action

## Install Library
```
pip install -r requirements.txt 
```

## Run or Open cypress
```
pytest -s     = run with debug
pytest -v     = run all test with desc
pytest        = run all test
```
## Module/file Explanation
```
.github/workflows               = folder/file to integrate with github action (exp: for running test in cloud)
.json_schema                    = folder/file to make template for validate response res with json schema 
.setting/case_management.py     = folder/file to integrate with test management tools (exp : QASE.IO)
.setting/endpoint.py            = folder/file to list our endpoint fo testing
.setting/general.py             = folder/file to setting our project run
.setting/notif_slack.py         = folder/file to integrate with slack (exp: notification test)
.test/conftest.py               = folder/file to make hooks test
.test                           = folder/file to make our test (exp: unit/e2e/integration/etc)
pytest.ini                      = folder/file to setting our pytest
```
