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


class Topology(object):
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
        "version": "int",
        "time_stamp": "datetime",
        "nodes": "list[Node]",
        "links": "list[Link]",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "version": "version",
        "time_stamp": "time_stamp",
        "nodes": "nodes",
        "links": "links",
    }

    def __init__(
        self,
        id=None,
        name=None,
        version=None,
        time_stamp=None,
        nodes=None,
        links=None,
    ):  # noqa: E501
        """Topology - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._version = None
        self._time_stamp = None
        self._nodes = None
        self._links = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.version = version
        self.time_stamp = time_stamp
        self.nodes = nodes
        self.links = links

    @property
    def id(self):
        """Gets the id of this Topology.  # noqa: E501


        :return: The id of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Topology.


        :param id: The id of this Topology.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError(
                "Invalid value for `id`, must not be `None`"
            )  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Topology.


        :param name: The name of this Topology.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this Topology.  # noqa: E501


        :return: The version of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Topology.


        :param version: The version of this Topology.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError(
                "Invalid value for `version`, must not be `None`"
            )  # noqa: E501

        self._version = version

    @property
    def time_stamp(self):
        """Gets the time_stamp of this Topology.  # noqa: E501


        :return: The time_stamp of this Topology.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this Topology.


        :param time_stamp: The time_stamp of this Topology.  # noqa: E501
        :type: datetime
        """
        if time_stamp is None:
            raise ValueError(
                "Invalid value for `time_stamp`, must not be `None`"
            )  # noqa: E501

        self._time_stamp = time_stamp

    @property
    def nodes(self):
        """Gets the nodes of this Topology.  # noqa: E501


        :return: The nodes of this Topology.  # noqa: E501
        :rtype: list[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Topology.


        :param nodes: The nodes of this Topology.  # noqa: E501
        :type: list[Node]
        """
        if nodes is None:
            raise ValueError(
                "Invalid value for `nodes`, must not be `None`"
            )  # noqa: E501

        self._nodes = nodes

    @property
    def links(self):
        """Gets the links of this Topology.  # noqa: E501


        :return: The links of this Topology.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Topology.


        :param links: The links of this Topology.  # noqa: E501
        :type: list[Link]
        """
        if links is None:
            raise ValueError(
                "Invalid value for `links`, must not be `None`"
            )  # noqa: E501

        self._links = links

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
        if issubclass(Topology, dict):
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
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
