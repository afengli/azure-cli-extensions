# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OperationResult(Model):
    """List of operations available at the listed Azure resource provider.

    :param name: The name of the operation.
    :type name: str
    :param display: The object that represents the operation.
    :type display:
     ~azure.mgmt.servicefabricmesh.models.AvailableOperationDisplay
    :param origin: Origin result
    :type origin: str
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'AvailableOperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, name=None, display=None, origin=None, next_link=None):
        super(OperationResult, self).__init__()
        self.name = name
        self.display = display
        self.origin = origin
        self.next_link = next_link