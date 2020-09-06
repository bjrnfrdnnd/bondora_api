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


class DebtManagementEvent(object):
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
        'created_on': 'datetime',
        'event_type': 'int',
        'description': 'str'
    }

    attribute_map = {
        'created_on': 'CreatedOn',
        'event_type': 'EventType',
        'description': 'Description'
    }

    def __init__(self, created_on=None, event_type=None, description=None):  # noqa: E501
        """DebtManagementEvent - a model defined in Swagger"""  # noqa: E501

        self._created_on = None
        self._event_type = None
        self._description = None
        self.discriminator = None

        if created_on is not None:
            self.created_on = created_on
        if event_type is not None:
            self.event_type = event_type
        if description is not None:
            self.description = description

    @property
    def created_on(self):
        """Gets the created_on of this DebtManagementEvent.  # noqa: E501

        Date of event  # noqa: E501

        :return: The created_on of this DebtManagementEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DebtManagementEvent.

        Date of event  # noqa: E501

        :param created_on: The created_on of this DebtManagementEvent.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def event_type(self):
        """Gets the event_type of this DebtManagementEvent.  # noqa: E501

        Type of event  # noqa: E501

        :return: The event_type of this DebtManagementEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this DebtManagementEvent.

        Type of event  # noqa: E501

        :param event_type: The event_type of this DebtManagementEvent.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 7, 9, 14, 15, 16, 20, 22, 23, 24, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def description(self):
        """Gets the description of this DebtManagementEvent.  # noqa: E501

        Type as a description, obsolete: use EventType  # noqa: E501

        :return: The description of this DebtManagementEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DebtManagementEvent.

        Type as a description, obsolete: use EventType  # noqa: E501

        :param description: The description of this DebtManagementEvent.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(DebtManagementEvent, dict):
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
        if not isinstance(other, DebtManagementEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other