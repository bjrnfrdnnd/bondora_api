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
from bondora_api.api.report_api import ReportApi  # noqa: E501
from bondora_api.rest import ApiException


class TestReportApi(unittest.TestCase):
    """ReportApi unit test stubs"""

    def setUp(self):
        self.api = bondora_api.api.report_api.ReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_report_generate_report(self):
        """Test case for report_generate_report

        Request to generate specified report type for set period.  # noqa: E501
        """
        pass

    def test_report_get_public_dataset(self):
        """Test case for report_get_public_dataset

        Provides daily public dataset of all loan data that is not covered by the data protection laws.  # noqa: E501
        """
        pass

    def test_report_get_report(self):
        """Test case for report_get_report

        Get report data for specified report identificator.  # noqa: E501
        """
        pass

    def test_report_get_report_list(self):
        """Test case for report_get_report_list

        List of all reports  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
