import pytest
import requests
import json
import logging

class test_requests(object):
    logging.basicConfig(level=logging.INFO)
    r=requests.get("https://www.baidu.com")
    logging.info(r)
    logging.info(r.text)
    logging.info(json.dumps(r.json(),indent=2))