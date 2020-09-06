# coding: utf-8

"""
    Bondora API V1

    Bondora API version 1  # noqa: E501

    OpenAPI spec version: v1
    Contact: investor@bondora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Debt(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_date': 'datetime',
        'end_date': 'datetime',
        'amount': 'str',
        'max_amount': 'str',
        'industry': 'str',
        'reporter': 'str'
    }

    attribute_map = {
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'amount': 'Amount',
        'max_amount': 'MaxAmount',
        'industry': 'Industry',
        'reporter': 'Reporter'
    }

    def __init__(self, start_date=None, end_date=None, amount=None, max_amount=None, industry=None, reporter=None):  # noqa: E501
        """Debt - a model defined in Swagger"""  # noqa: E501

        self._start_date = None
        self._end_date = None
        self._amount = None
        self._max_amount = None
        self._industry = None
        self._reporter = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if amount is not None:
            self.amount = amount
        if max_amount is not None:
            self.max_amount = max_amount
        if industry is not None:
            self.industry = industry
        if reporter is not None:
            self.reporter = reporter

    @property
    def start_date(self):
        """Gets the start_date of this Debt.  # noqa: E501

        Start  # noqa: E501

        :return: The start_date of this Debt.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Debt.

        Start  # noqa: E501

        :param start_date: The start_date of this Debt.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Debt.  # noqa: E501

        End  # noqa: E501

        :return: The end_date of this Debt.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Debt.

        End  # noqa: E501

        :param end_date: The end_date of this Debt.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def amount(self):
        """Gets the amount of this Debt.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Debt.

        Amount  # noqa: E501

        :param amount: The amount of this Debt.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def max_amount(self):
        """Gets the max_amount of this Debt.  # noqa: E501

        Max amount  # noqa: E501

        :return: The max_amount of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """Sets the max_amount of this Debt.

        Max amount  # noqa: E501

        :param max_amount: The max_amount of this Debt.  # noqa: E501
        :type: str
        """

        self._max_amount = max_amount

    @property
    def industry(self):
        """Gets the industry of this Debt.  # noqa: E501

        Industry  # noqa: E501

        :return: The industry of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this Debt.

        Industry  # noqa: E501

        :param industry: The industry of this Debt.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def reporter(self):
        """Gets the reporter of this Debt.  # noqa: E501

        Reporter  # noqa: E501

        :return: The reporter of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._reporter

    @reporter.setter
    def reporter(self, reporter):
        """Sets the reporter of this Debt.

        Reporter  # noqa: E501

        :param reporter: The reporter of this Debt.  # noqa: E501
        :type: str
        """

        self._reporter = reporter

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Debt, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Debt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other