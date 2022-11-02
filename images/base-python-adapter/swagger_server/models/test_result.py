# coding: utf-8

#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TestResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, error_message: str=None):  # noqa: E501
        """TestResult - a model defined in Swagger

        :param error_message: The error_message of this TestResult.  # noqa: E501
        :type error_message: str
        """
        self.swagger_types = {
            'error_message': str
        }

        self.attribute_map = {
            'error_message': 'errorMessage'
        }
        self._error_message = error_message

    @classmethod
    def from_dict(cls, dikt) -> 'TestResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TestResult of this TestResult.  # noqa: E501
        :rtype: TestResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def error_message(self) -> str:
        """Gets the error_message of this TestResult.

        Contains the error message if the test connection failed.  # noqa: E501

        :return: The error_message of this TestResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message: str):
        """Sets the error_message of this TestResult.

        Contains the error message if the test connection failed.  # noqa: E501

        :param error_message: The error_message of this TestResult.
        :type error_message: str
        """

        self._error_message = error_message