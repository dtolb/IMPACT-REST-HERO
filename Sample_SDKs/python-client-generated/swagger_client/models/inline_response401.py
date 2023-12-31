# coding: utf-8

"""

    This is the API for the Pet Store.  # noqa: E501

    OpenAPI spec version: 1.0.0-rev1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.error_body import ErrorBody  # noqa: F401,E501

class InlineResponse401(ErrorBody):
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
        'message': 'str'
    }
    if hasattr(ErrorBody, "swagger_types"):
        swagger_types.update(ErrorBody.swagger_types)

    attribute_map = {
        'message': 'message'
    }
    if hasattr(ErrorBody, "attribute_map"):
        attribute_map.update(ErrorBody.attribute_map)

    def __init__(self, message=None, *args, **kwargs):  # noqa: E501
        """InlineResponse401 - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self.discriminator = None
        self.message = message
        ErrorBody.__init__(self, *args, **kwargs)

    @property
    def message(self):
        """Gets the message of this InlineResponse401.  # noqa: E501


        :return: The message of this InlineResponse401.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse401.


        :param message: The message of this InlineResponse401.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501
        allowed_values = ["User is not authorized"]  # noqa: E501
        if message not in allowed_values:
            raise ValueError(
                "Invalid value for `message` ({0}), must be one of {1}"  # noqa: E501
                .format(message, allowed_values)
            )

        self._message = message

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
        if issubclass(InlineResponse401, dict):
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
        if not isinstance(other, InlineResponse401):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
