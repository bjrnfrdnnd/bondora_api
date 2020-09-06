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


class ApiResultEventLog(object):
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
        'page_size': 'int',
        'page_nr': 'int',
        'total_count': 'int',
        'count': 'int',
        'payload': 'list[EventLogItem]',
        'success': 'bool',
        'errors': 'list[ApiError]'
    }

    attribute_map = {
        'page_size': 'PageSize',
        'page_nr': 'PageNr',
        'total_count': 'TotalCount',
        'count': 'Count',
        'payload': 'Payload',
        'success': 'Success',
        'errors': 'Errors'
    }

    def __init__(self, page_size=None, page_nr=None, total_count=None, count=None, payload=None, success=None, errors=None):  # noqa: E501
        """ApiResultEventLog - a model defined in Swagger"""  # noqa: E501

        self._page_size = None
        self._page_nr = None
        self._total_count = None
        self._count = None
        self._payload = None
        self._success = None
        self._errors = None
        self.discriminator = None

        if page_size is not None:
            self.page_size = page_size
        if page_nr is not None:
            self.page_nr = page_nr
        self.total_count = total_count
        self.count = count
        if payload is not None:
            self.payload = payload
        self.success = success
        if errors is not None:
            self.errors = errors

    @property
    def page_size(self):
        """Gets the page_size of this ApiResultEventLog.  # noqa: E501

        Requested Max items in result  # noqa: E501

        :return: The page_size of this ApiResultEventLog.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ApiResultEventLog.

        Requested Max items in result  # noqa: E501

        :param page_size: The page_size of this ApiResultEventLog.  # noqa: E501
        :type: int
        """
        if page_size is not None and page_size > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if page_size is not None and page_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._page_size = page_size

    @property
    def page_nr(self):
        """Gets the page_nr of this ApiResultEventLog.  # noqa: E501

        Requested page nr  # noqa: E501

        :return: The page_nr of this ApiResultEventLog.  # noqa: E501
        :rtype: int
        """
        return self._page_nr

    @page_nr.setter
    def page_nr(self, page_nr):
        """Sets the page_nr of this ApiResultEventLog.

        Requested page nr  # noqa: E501

        :param page_nr: The page_nr of this ApiResultEventLog.  # noqa: E501
        :type: int
        """
        if page_nr is not None and page_nr > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `page_nr`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if page_nr is not None and page_nr < 1:  # noqa: E501
            raise ValueError("Invalid value for `page_nr`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_nr = page_nr

    @property
    def total_count(self):
        """Gets the total_count of this ApiResultEventLog.  # noqa: E501

        Total number of items found  # noqa: E501

        :return: The total_count of this ApiResultEventLog.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ApiResultEventLog.

        Total number of items found  # noqa: E501

        :param total_count: The total_count of this ApiResultEventLog.  # noqa: E501
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501
        if total_count is not None and total_count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if total_count is not None and total_count < 0:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._total_count = total_count

    @property
    def count(self):
        """Gets the count of this ApiResultEventLog.  # noqa: E501

        Number of items returned  # noqa: E501

        :return: The count of this ApiResultEventLog.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ApiResultEventLog.

        Number of items returned  # noqa: E501

        :param count: The count of this ApiResultEventLog.  # noqa: E501
        :type: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501
        if count is not None and count > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if count is not None and count < 0:  # noqa: E501
            raise ValueError("Invalid value for `count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._count = count

    @property
    def payload(self):
        """Gets the payload of this ApiResultEventLog.  # noqa: E501

        The payload of the response. Type depends on the API request.  # noqa: E501

        :return: The payload of this ApiResultEventLog.  # noqa: E501
        :rtype: list[EventLogItem]
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ApiResultEventLog.

        The payload of the response. Type depends on the API request.  # noqa: E501

        :param payload: The payload of this ApiResultEventLog.  # noqa: E501
        :type: list[EventLogItem]
        """

        self._payload = payload

    @property
    def success(self):
        """Gets the success of this ApiResultEventLog.  # noqa: E501

        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.  # noqa: E501

        :return: The success of this ApiResultEventLog.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ApiResultEventLog.

        Indicates if the request was successfull or not.              true if the request was handled successfully, false otherwise.  # noqa: E501

        :param success: The success of this ApiResultEventLog.  # noqa: E501
        :type: bool
        """
        if success is None:
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def errors(self):
        """Gets the errors of this ApiResultEventLog.  # noqa: E501

        Error(s) accociated with the API request.  # noqa: E501

        :return: The errors of this ApiResultEventLog.  # noqa: E501
        :rtype: list[ApiError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ApiResultEventLog.

        Error(s) accociated with the API request.  # noqa: E501

        :param errors: The errors of this ApiResultEventLog.  # noqa: E501
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
        if issubclass(ApiResultEventLog, dict):
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
        if not isinstance(other, ApiResultEventLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
