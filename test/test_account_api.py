# coding: utf-8

"""
    Bondora API V1

    Bondora API version 1  # noqa: E501

    OpenAPI spec version: v1
    Contact: investor@bondora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.account_api import AccountApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.account_api.AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_get_active(self):
        """Test case for account_get_active

        Gets list of your investments  # noqa: E501
        """
        pass

    def test_account_get_balance(self):
        """Test case for account_get_balance

        Gets your account balance information  # noqa: E501
        """
        pass

    def test_account_get_event_log(self):
        """Test case for account_get_event_log

        Gets events that have been made with this application (related to current access token)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
