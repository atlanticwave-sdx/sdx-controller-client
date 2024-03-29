# coding: utf-8

"""
    SDX-Controller

    You can find out more about Swagger at
    [http://swagger.io](http://swagger.io) or on [irc.freenode.net,
    #swagger](http://swagger.io/irc/).

    OpenAPI spec version: 1.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Node(object):
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
        "id": "str",
        "name": "str",
        "short_name": "str",
        "ports": "list[Port]",
        "location": "Location",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "short_name": "short_name",
        "ports": "ports",
        "location": "location",
    }

    def __init__(
        self, id=None, name=None, short_name=None, ports=None, location=None
    ):  # noqa: E501
        """Node - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._short_name = None
        self._ports = None
        self._location = None
        self.discriminator = None
        self.id = id
        self.name = name
        if short_name is not None:
            self.short_name = short_name
        self.ports = ports
        self.location = location

    @property
    def id(self):
        """Gets the id of this Node.  # noqa: E501


        :return: The id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.


        :param id: The id of this Node.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError(
                "Invalid value for `id`, must not be `None`"
            )  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Node.  # noqa: E501


        :return: The name of this Node.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.


        :param name: The name of this Node.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Node.  # noqa: E501


        :return: The short_name of this Node.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Node.


        :param short_name: The short_name of this Node.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def ports(self):
        """Gets the ports of this Node.  # noqa: E501


        :return: The ports of this Node.  # noqa: E501
        :rtype: list[Port]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Node.


        :param ports: The ports of this Node.  # noqa: E501
        :type: list[Port]
        """
        if ports is None:
            raise ValueError(
                "Invalid value for `ports`, must not be `None`"
            )  # noqa: E501

        self._ports = ports

    @property
    def location(self):
        """Gets the location of this Node.  # noqa: E501


        :return: The location of this Node.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Node.


        :param location: The location of this Node.  # noqa: E501
        :type: Location
        """
        if location is None:
            raise ValueError(
                "Invalid value for `location`, must not be `None`"
            )  # noqa: E501

        self._location = location

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value,
                    )
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Node, dict):
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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
