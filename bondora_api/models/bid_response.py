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


class BidResponse(object):
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
        'id': 'str',
        'auction_id': 'str',
        'amount': 'float',
        'min_amount': 'float'
    }

    attribute_map = {
        'id': 'Id',
        'auction_id': 'AuctionId',
        'amount': 'Amount',
        'min_amount': 'MinAmount'
    }

    def __init__(self, id=None, auction_id=None, amount=None, min_amount=None):  # noqa: E501
        """BidResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._auction_id = None
        self._amount = None
        self._min_amount = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if auction_id is not None:
            self.auction_id = auction_id
        if amount is not None:
            self.amount = amount
        if min_amount is not None:
            self.min_amount = min_amount

    @property
    def id(self):
        """Gets the id of this BidResponse.  # noqa: E501

        Item unique identifier  # noqa: E501

        :return: The id of this BidResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BidResponse.

        Item unique identifier  # noqa: E501

        :param id: The id of this BidResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def auction_id(self):
        """Gets the auction_id of this BidResponse.  # noqa: E501

        Auction unique identifier  # noqa: E501

        :return: The auction_id of this BidResponse.  # noqa: E501
        :rtype: str
        """
        return self._auction_id

    @auction_id.setter
    def auction_id(self, auction_id):
        """Sets the auction_id of this BidResponse.

        Auction unique identifier  # noqa: E501

        :param auction_id: The auction_id of this BidResponse.  # noqa: E501
        :type: str
        """

        self._auction_id = auction_id

    @property
    def amount(self):
        """Gets the amount of this BidResponse.  # noqa: E501

        Amount to bid into Auction  # noqa: E501

        :return: The amount of this BidResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BidResponse.

        Amount to bid into Auction  # noqa: E501

        :param amount: The amount of this BidResponse.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def min_amount(self):
        """Gets the min_amount of this BidResponse.  # noqa: E501

        Not used. Will always be NULL.  # noqa: E501

        :return: The min_amount of this BidResponse.  # noqa: E501
        :rtype: float
        """
        return self._min_amount

    @min_amount.setter
    def min_amount(self, min_amount):
        """Sets the min_amount of this BidResponse.

        Not used. Will always be NULL.  # noqa: E501

        :param min_amount: The min_amount of this BidResponse.  # noqa: E501
        :type: float
        """

        self._min_amount = min_amount

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
        if issubclass(BidResponse, dict):
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
        if not isinstance(other, BidResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other