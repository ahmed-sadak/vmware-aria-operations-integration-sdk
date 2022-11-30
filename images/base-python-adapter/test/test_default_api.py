# coding: utf-8
"""
    Adapter API

    The API contract is defined using a standard OpenAPI specification to simplify adapter development.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""
#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0
from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_collect(self):
        """Test case for collect

        Data Collection  # noqa: E501
        """
        pass

    def test_get_endpoint_urls(self):
        """Test case for get_endpoint_urls

        Retrieve endpoint URLs  # noqa: E501
        """
        pass

    def test_test(self):
        """Test case for test

        Connection Test  # noqa: E501
        """
        pass

    def test_version(self):
        """Test case for version

        Adapter Version  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
