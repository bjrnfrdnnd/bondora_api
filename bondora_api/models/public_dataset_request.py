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


class PublicDatasetRequest(object):
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
        'loan_ids': 'list[str]',
        'countries': 'list[str]',
        'ratings': 'list[str]',
        'loan_date_from': 'datetime',
        'loan_date_to': 'datetime',
        'page_size': 'int',
        'page_nr': 'int'
    }

    attribute_map = {
        'loan_ids': 'LoanIds',
        'countries': 'Countries',
        'ratings': 'Ratings',
        'loan_date_from': 'LoanDateFrom',
        'loan_date_to': 'LoanDateTo',
        'page_size': 'PageSize',
        'page_nr': 'PageNr'
    }

    def __init__(self, loan_ids=None, countries=None, ratings=None, loan_date_from=None, loan_date_to=None, page_size=None, page_nr=None):  # noqa: E501
        """PublicDatasetRequest - a model defined in Swagger"""  # noqa: E501

        self._loan_ids = None
        self._countries = None
        self._ratings = None
        self._loan_date_from = None
        self._loan_date_to = None
        self._page_size = None
        self._page_nr = None
        self.discriminator = None

        if loan_ids is not None:
            self.loan_ids = loan_ids
        if countries is not None:
            self.countries = countries
        if ratings is not None:
            self.ratings = ratings
        if loan_date_from is not None:
            self.loan_date_from = loan_date_from
        if loan_date_to is not None:
            self.loan_date_to = loan_date_to
        if page_size is not None:
            self.page_size = page_size
        if page_nr is not None:
            self.page_nr = page_nr

    @property
    def loan_ids(self):
        """Gets the loan_ids of this PublicDatasetRequest.  # noqa: E501

        Specific loans to search  # noqa: E501

        :return: The loan_ids of this PublicDatasetRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._loan_ids

    @loan_ids.setter
    def loan_ids(self, loan_ids):
        """Sets the loan_ids of this PublicDatasetRequest.

        Specific loans to search  # noqa: E501

        :param loan_ids: The loan_ids of this PublicDatasetRequest.  # noqa: E501
        :type: list[str]
        """

        self._loan_ids = loan_ids

    @property
    def countries(self):
        """Gets the countries of this PublicDatasetRequest.  # noqa: E501

        Two letter iso code for country of origin: EE, ES, FI  # noqa: E501

        :return: The countries of this PublicDatasetRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this PublicDatasetRequest.

        Two letter iso code for country of origin: EE, ES, FI  # noqa: E501

        :param countries: The countries of this PublicDatasetRequest.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def ratings(self):
        """Gets the ratings of this PublicDatasetRequest.  # noqa: E501

        Bondora's rating: AA, A, B, C, D, E, F, HR  # noqa: E501

        :return: The ratings of this PublicDatasetRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this PublicDatasetRequest.

        Bondora's rating: AA, A, B, C, D, E, F, HR  # noqa: E501

        :param ratings: The ratings of this PublicDatasetRequest.  # noqa: E501
        :type: list[str]
        """

        self._ratings = ratings

    @property
    def loan_date_from(self):
        """Gets the loan_date_from of this PublicDatasetRequest.  # noqa: E501

        Loan start date from  # noqa: E501

        :return: The loan_date_from of this PublicDatasetRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._loan_date_from

    @loan_date_from.setter
    def loan_date_from(self, loan_date_from):
        """Sets the loan_date_from of this PublicDatasetRequest.

        Loan start date from  # noqa: E501

        :param loan_date_from: The loan_date_from of this PublicDatasetRequest.  # noqa: E501
        :type: datetime
        """

        self._loan_date_from = loan_date_from

    @property
    def loan_date_to(self):
        """Gets the loan_date_to of this PublicDatasetRequest.  # noqa: E501

        Loan start date to  # noqa: E501

        :return: The loan_date_to of this PublicDatasetRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._loan_date_to

    @loan_date_to.setter
    def loan_date_to(self, loan_date_to):
        """Sets the loan_date_to of this PublicDatasetRequest.

        Loan start date to  # noqa: E501

        :param loan_date_to: The loan_date_to of this PublicDatasetRequest.  # noqa: E501
        :type: datetime
        """

        self._loan_date_to = loan_date_to

    @property
    def page_size(self):
        """Gets the page_size of this PublicDatasetRequest.  # noqa: E501

        Max items in result, up to 10000  # noqa: E501

        :return: The page_size of this PublicDatasetRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PublicDatasetRequest.

        Max items in result, up to 10000  # noqa: E501

        :param page_size: The page_size of this PublicDatasetRequest.  # noqa: E501
        :type: int
        """
        if page_size is not None and page_size > 10000:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `10000`")  # noqa: E501
        if page_size is not None and page_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_size = page_size

    @property
    def page_nr(self):
        """Gets the page_nr of this PublicDatasetRequest.  # noqa: E501

        Result page nr  # noqa: E501

        :return: The page_nr of this PublicDatasetRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_nr

    @page_nr.setter
    def page_nr(self, page_nr):
        """Sets the page_nr of this PublicDatasetRequest.

        Result page nr  # noqa: E501

        :param page_nr: The page_nr of this PublicDatasetRequest.  # noqa: E501
        :type: int
        """
        if page_nr is not None and page_nr > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `page_nr`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if page_nr is not None and page_nr < 1:  # noqa: E501
            raise ValueError("Invalid value for `page_nr`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_nr = page_nr

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
        if issubclass(PublicDatasetRequest, dict):
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
        if not isinstance(other, PublicDatasetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
