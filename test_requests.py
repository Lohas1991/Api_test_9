import pytest
import requests
import json
import logging

class test_requests(object):
    logging.basicConfig(level=logging.INFO)
    r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
    logging.info(r)
    logging.info(r.text)
    logging.info(json.dumps(r.json(),indent=2))