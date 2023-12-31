# coding: utf-8

"""

    This is the API for the Pet Store.  # noqa: E501

    OpenAPI spec version: 1.0.0-rev1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ListPetsHeaders(object):
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
        'tracking_id': 'str',
        '_date': 'str',
        'link': 'str'
    }

    attribute_map = {
        'tracking_id': 'TrackingId',
        '_date': 'Date',
        'link': 'link'
    }

    def __init__(self, tracking_id=None, _date=None, link=None):  # noqa: E501
        """ListPetsHeaders - a model defined in Swagger"""  # noqa: E501
        self._tracking_id = None
        self.__date = None
        self._link = None
        self.discriminator = None
        self.tracking_id = tracking_id
        self._date = _date
        self.link = link

    @property
    def tracking_id(self):
        """Gets the tracking_id of this ListPetsHeaders.  # noqa: E501

        Track each request's by this ID  # noqa: E501

        :return: The tracking_id of this ListPetsHeaders.  # noqa: E501
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id):
        """Sets the tracking_id of this ListPetsHeaders.

        Track each request's by this ID  # noqa: E501

        :param tracking_id: The tracking_id of this ListPetsHeaders.  # noqa: E501
        :type: str
        """
        if tracking_id is None:
            raise ValueError("Invalid value for `tracking_id`, must not be `None`")  # noqa: E501

        self._tracking_id = tracking_id

    @property
    def _date(self):
        """Gets the _date of this ListPetsHeaders.  # noqa: E501

        datetime of the request  # noqa: E501

        :return: The _date of this ListPetsHeaders.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ListPetsHeaders.

        datetime of the request  # noqa: E501

        :param _date: The _date of this ListPetsHeaders.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def link(self):
        """Gets the link of this ListPetsHeaders.  # noqa: E501

        the URL to request more pets  # noqa: E501

        :return: The link of this ListPetsHeaders.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ListPetsHeaders.

        the URL to request more pets  # noqa: E501

        :param link: The link of this ListPetsHeaders.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

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
        if issubclass(ListPetsHeaders, dict):
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
        if not isinstance(other, ListPetsHeaders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
