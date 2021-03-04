import pytest
import requests
import json
import logging

class TestRequests(object):
    url="https://testerhome.com/api/v3/topics.json?limit=2"
    def __init__(self,filename):
        self.logger=logging.getLogger("requests")
        self.logger.setLevel(logging.DEBUG)
        fmt=logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s","%Y-%m-%d %H:%M:%S")
        #logging.basicConfig(filename="req.log")
        fh=logging.FileHandler(filename)
        fh.setFormatter(fmt)
        fh.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)
    
    def test_get(self):
        r=requests.get(self.url)
        #logging.info(r)
        #logging.info(r.text)
        #logging.info(json.dumps(r.json(),indent=2))
        self.logger.info(r)
        self.logger.info(r.text)
        self.logger.info(json.dumps(r.json(),indent=2))
if __name__ == '__main__':
    request=TestRequests('requests.log')
    request.test_get()
   #def test_post(self):
