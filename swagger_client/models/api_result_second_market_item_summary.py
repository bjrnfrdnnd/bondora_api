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


class ApiResultSecondMarketItemSummary(object):
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
        'payload': 'SecondMarketItemSummary',
        'success': 'bool',
        'errors': 'list[ApiError]'
    }

    attribute_map = {
        'payload': 'Payload',
        'success': 'Success',
        'errors': 'Errors'
    }

    def __init__(self, payload=None, success=None, errors=None):  # noqa: E501
        """ApiResultSecondMarketItemSummary - a model defined in Swagger"""  # noqa: E501

        self._payload = None
        self._success = None
        self._errors = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload
        self.success = success
        if errors is not None:
            self.errors = errors

    @property
    def payload(self):
        """Gets the payload of this ApiResultSecondMarketItemSummary.  # noqa: E501

        The payload of the response. Type depends on the API request.  # noqa: E501

        :return: The payload of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :rtype: SecondMarketItemSummary
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ApiResultSecondMarketItemSummary.

        The payload of the response. Type depends on the API request.  # noqa: E501

        :param payload: The payload of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :type: SecondMarketItemSummary
        """

        self._payload = payload

    @property
    def success(self):
        """Gets the success of this ApiResultSecondMarketItemSummary.  # noqa: E501

        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.  # noqa: E501

        :return: The success of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ApiResultSecondMarketItemSummary.

        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.  # noqa: E501

        :param success: The success of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def errors(self):
        """Gets the errors of this ApiResultSecondMarketItemSummary.  # noqa: E501

        Error(s) accociated with the API request.  # noqa: E501

        :return: The errors of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :rtype: list[ApiError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApiResultSecondMarketItemSummary.

        Error(s) accociated with the API request.  # noqa: E501

        :param errors: The errors of this ApiResultSecondMarketItemSummary.  # noqa: E501
        :type: list[ApiError]
        """

        self._errors = errors

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
        if issubclass(ApiResultSecondMarketItemSummary, dict):
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
        if not isinstance(other, ApiResultSecondMarketItemSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
