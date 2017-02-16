# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ContainerStateTerminated(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, container_id=None, exit_code=None, finished_at=None, message=None, reason=None, signal=None, started_at=None):
        """
        V1ContainerStateTerminated - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'container_id': 'str',
            'exit_code': 'int',
            'finished_at': 'UnversionedTime',
            'message': 'str',
            'reason': 'str',
            'signal': 'int',
            'started_at': 'UnversionedTime'
        }

        self.attribute_map = {
            'container_id': 'containerID',
            'exit_code': 'exitCode',
            'finished_at': 'finishedAt',
            'message': 'message',
            'reason': 'reason',
            'signal': 'signal',
            'started_at': 'startedAt'
        }

        self._container_id = container_id
        self._exit_code = exit_code
        self._finished_at = finished_at
        self._message = message
        self._reason = reason
        self._signal = signal
        self._started_at = started_at

    @property
    def container_id(self):
        """
        Gets the container_id of this V1ContainerStateTerminated.
        Container's ID in the format 'docker://<container_id>'

        :return: The container_id of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this V1ContainerStateTerminated.
        Container's ID in the format 'docker://<container_id>'

        :param container_id: The container_id of this V1ContainerStateTerminated.
        :type: str
        """

        self._container_id = container_id

    @property
    def exit_code(self):
        """
        Gets the exit_code of this V1ContainerStateTerminated.
        Exit status from the last termination of the container

        :return: The exit_code of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """
        Sets the exit_code of this V1ContainerStateTerminated.
        Exit status from the last termination of the container

        :param exit_code: The exit_code of this V1ContainerStateTerminated.
        :type: int
        """
        if exit_code is None:
            raise ValueError("Invalid value for `exit_code`, must not be `None`")

        self._exit_code = exit_code

    @property
    def finished_at(self):
        """
        Gets the finished_at of this V1ContainerStateTerminated.
        Time at which the container last terminated

        :return: The finished_at of this V1ContainerStateTerminated.
        :rtype: UnversionedTime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """
        Sets the finished_at of this V1ContainerStateTerminated.
        Time at which the container last terminated

        :param finished_at: The finished_at of this V1ContainerStateTerminated.
        :type: UnversionedTime
        """

        self._finished_at = finished_at

    @property
    def message(self):
        """
        Gets the message of this V1ContainerStateTerminated.
        Message regarding the last termination of the container

        :return: The message of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1ContainerStateTerminated.
        Message regarding the last termination of the container

        :param message: The message of this V1ContainerStateTerminated.
        :type: str
        """

        self._message = message

    @property
    def reason(self):
        """
        Gets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :return: The reason of this V1ContainerStateTerminated.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this V1ContainerStateTerminated.
        (brief) reason from the last termination of the container

        :param reason: The reason of this V1ContainerStateTerminated.
        :type: str
        """

        self._reason = reason

    @property
    def signal(self):
        """
        Gets the signal of this V1ContainerStateTerminated.
        Signal from the last termination of the container

        :return: The signal of this V1ContainerStateTerminated.
        :rtype: int
        """
        return self._signal

    @signal.setter
    def signal(self, signal):
        """
        Sets the signal of this V1ContainerStateTerminated.
        Signal from the last termination of the container

        :param signal: The signal of this V1ContainerStateTerminated.
        :type: int
        """

        self._signal = signal

    @property
    def started_at(self):
        """
        Gets the started_at of this V1ContainerStateTerminated.
        Time at which previous execution of the container started

        :return: The started_at of this V1ContainerStateTerminated.
        :rtype: UnversionedTime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this V1ContainerStateTerminated.
        Time at which previous execution of the container started

        :param started_at: The started_at of this V1ContainerStateTerminated.
        :type: UnversionedTime
        """

        self._started_at = started_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
