# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.vet import Vet  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVetResourceController(BaseTestCase):
    """VetResourceController integration test stubs"""

    def test_show_resources_vet_list_using_get(self):
        """Test case for show_resources_vet_list_using_get

        showResourcesVetList
        """
        response = self.client.open(
            '//vets',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
