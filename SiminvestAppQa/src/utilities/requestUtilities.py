import requests
import json
import logging as logger
import allure




class RequestsUtilities(object):


    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f'Bad Status code.' \
                                                              f"Expected{self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    logger.info("Post Request for the API")

    @allure.step("Post request")
    def post(self, base_url,endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}
        self.url = base_url + endpoint
        rs_api = requests.post(self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Post response:{self.rs_json} ")
        return self.rs_json

    logger.info("Get Request of the API")

    @allure.step("Get request")
    def get(self, base_url, endpoint, payload=None, headers=None, params=None,expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = base_url + endpoint
        rs_api = requests.get(self.url, data=payload, headers=headers, params=params)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"API Get response:{self.rs_json} ")
        return self.rs_json

