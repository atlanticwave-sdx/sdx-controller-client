# coding: utf-8

"""
    SDX-Controller

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.link_api import LinkApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLinkApi(unittest.TestCase):
    """LinkApi unit test stubs"""

    def setUp(self):
        self.api = LinkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_link(self):
        """Test case for get_link

        get an existing link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
