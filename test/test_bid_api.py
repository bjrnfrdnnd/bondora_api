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

import bondora_api
from bondora_api.api.bid_api import BidApi  # noqa: E501
from bondora_api.rest import ApiException


class TestBidApi(unittest.TestCase):
    """BidApi unit test stubs"""

    def setUp(self):
        self.api = bondora_api.api.bid_api.BidApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bid_cancel_bid(self):
        """Test case for bid_cancel_bid

        Cancel the Bid  # noqa: E501
        """
        pass

    def test_bid_get_bid(self):
        """Test case for bid_get_bid

        Get the Bid  # noqa: E501
        """
        pass

    def test_bid_get_bid_summaries(self):
        """Test case for bid_get_bid_summaries

        Gets list of bids the investor has made.  # noqa: E501
        """
        pass

    def test_bid_make_bids(self):
        """Test case for bid_make_bids

        Makes bid(s) into specified auction(s).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
