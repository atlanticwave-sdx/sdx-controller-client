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


class Link(object):
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
        "bandwidth": "float",
        "residual_bandwidth": "float",
        "latency": "float",
        "packet_loss": "float",
        "availability": "float",
        "state": "str",
        "status": "str",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "short_name": "short_name",
        "ports": "ports",
        "bandwidth": "bandwidth",
        "residual_bandwidth": "residual_bandwidth",
        "latency": "latency",
        "packet_loss": "packet_loss",
        "availability": "availability",
        "state": "state",
        "status": "status",
    }

    def __init__(
        self,
        id=None,
        name=None,
        short_name=None,
        ports=None,
        bandwidth=None,
        residual_bandwidth=None,
        latency=None,
        packet_loss=None,
        availability=None,
        state=None,
        status=None,
    ):  # noqa: E501
        """Link - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._short_name = None
        self._ports = None
        self._bandwidth = None
        self._residual_bandwidth = None
        self._latency = None
        self._packet_loss = None
        self._availability = None
        self._state = None
        self._status = None
        self.discriminator = None
        self.id = id
        self.name = name
        if short_name is not None:
            self.short_name = short_name
        self.ports = ports
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if residual_bandwidth is not None:
            self.residual_bandwidth = residual_bandwidth
        if latency is not None:
            self.latency = latency
        if packet_loss is not None:
            self.packet_loss = packet_loss
        if availability is not None:
            self.availability = availability
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Link.  # noqa: E501


        :return: The id of this Link.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Link.


        :param id: The id of this Link.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError(
                "Invalid value for `id`, must not be `None`"
            )  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Link.  # noqa: E501


        :return: The name of this Link.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Link.


        :param name: The name of this Link.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def short_name(self):
        """Gets the short_name of this Link.  # noqa: E501


        :return: The short_name of this Link.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Link.


        :param short_name: The short_name of this Link.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def ports(self):
        """Gets the ports of this Link.  # noqa: E501


        :return: The ports of this Link.  # noqa: E501
        :rtype: list[Port]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Link.


        :param ports: The ports of this Link.  # noqa: E501
        :type: list[Port]
        """
        if ports is None:
            raise ValueError(
                "Invalid value for `ports`, must not be `None`"
            )  # noqa: E501

        self._ports = ports

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Link.  # noqa: E501


        :return: The bandwidth of this Link.  # noqa: E501
        :rtype: float
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Link.


        :param bandwidth: The bandwidth of this Link.  # noqa: E501
        :type: float
        """

        self._bandwidth = bandwidth

    @property
    def residual_bandwidth(self):
        """Gets the residual_bandwidth of this Link.  # noqa: E501


        :return: The residual_bandwidth of this Link.  # noqa: E501
        :rtype: float
        """
        return self._residual_bandwidth

    @residual_bandwidth.setter
    def residual_bandwidth(self, residual_bandwidth):
        """Sets the residual_bandwidth of this Link.


        :param residual_bandwidth: The residual_bandwidth of this Link.  # noqa: E501
        :type: float
        """

        self._residual_bandwidth = residual_bandwidth

    @property
    def latency(self):
        """Gets the latency of this Link.  # noqa: E501


        :return: The latency of this Link.  # noqa: E501
        :rtype: float
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this Link.


        :param latency: The latency of this Link.  # noqa: E501
        :type: float
        """

        self._latency = latency

    @property
    def packet_loss(self):
        """Gets the packet_loss of this Link.  # noqa: E501


        :return: The packet_loss of this Link.  # noqa: E501
        :rtype: float
        """
        return self._packet_loss

    @packet_loss.setter
    def packet_loss(self, packet_loss):
        """Sets the packet_loss of this Link.


        :param packet_loss: The packet_loss of this Link.  # noqa: E501
        :type: float
        """

        self._packet_loss = packet_loss

    @property
    def availability(self):
        """Gets the availability of this Link.  # noqa: E501


        :return: The availability of this Link.  # noqa: E501
        :rtype: float
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this Link.


        :param availability: The availability of this Link.  # noqa: E501
        :type: float
        """

        self._availability = availability

    @property
    def state(self):
        """Gets the state of this Link.  # noqa: E501


        :return: The state of this Link.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Link.


        :param state: The state of this Link.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this Link.  # noqa: E501


        :return: The status of this Link.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Link.


        :param status: The status of this Link.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(Link, dict):
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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
