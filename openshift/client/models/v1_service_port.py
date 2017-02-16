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


class V1ServicePort(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, node_port=None, port=None, protocol=None, target_port=None):
        """
        V1ServicePort - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'node_port': 'int',
            'port': 'int',
            'protocol': 'str',
            'target_port': 'IntstrIntOrString'
        }

        self.attribute_map = {
            'name': 'name',
            'node_port': 'nodePort',
            'port': 'port',
            'protocol': 'protocol',
            'target_port': 'targetPort'
        }

        self._name = name
        self._node_port = node_port
        self._port = port
        self._protocol = protocol
        self._target_port = target_port

    @property
    def name(self):
        """
        Gets the name of this V1ServicePort.
        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.

        :return: The name of this V1ServicePort.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ServicePort.
        The name of this port within the service. This must be a DNS_LABEL. All ports within a ServiceSpec must have unique names. This maps to the 'Name' field in EndpointPort objects. Optional if only one ServicePort is defined on this service.

        :param name: The name of this V1ServicePort.
        :type: str
        """

        self._name = name

    @property
    def node_port(self):
        """
        Gets the node_port of this V1ServicePort.
        The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: http://kubernetes.io/docs/user-guide/services#type--nodeport

        :return: The node_port of this V1ServicePort.
        :rtype: int
        """
        return self._node_port

    @node_port.setter
    def node_port(self, node_port):
        """
        Sets the node_port of this V1ServicePort.
        The port on each node on which this service is exposed when type=NodePort or LoadBalancer. Usually assigned by the system. If specified, it will be allocated to the service if unused or else creation of the service will fail. Default is to auto-allocate a port if the ServiceType of this Service requires one. More info: http://kubernetes.io/docs/user-guide/services#type--nodeport

        :param node_port: The node_port of this V1ServicePort.
        :type: int
        """

        self._node_port = node_port

    @property
    def port(self):
        """
        Gets the port of this V1ServicePort.
        The port that will be exposed by this service.

        :return: The port of this V1ServicePort.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1ServicePort.
        The port that will be exposed by this service.

        :param port: The port of this V1ServicePort.
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this V1ServicePort.
        The IP protocol for this port. Supports \"TCP\" and \"UDP\". Default is TCP.

        :return: The protocol of this V1ServicePort.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this V1ServicePort.
        The IP protocol for this port. Supports \"TCP\" and \"UDP\". Default is TCP.

        :param protocol: The protocol of this V1ServicePort.
        :type: str
        """

        self._protocol = protocol

    @property
    def target_port(self):
        """
        Gets the target_port of this V1ServicePort.
        Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: http://kubernetes.io/docs/user-guide/services#defining-a-service

        :return: The target_port of this V1ServicePort.
        :rtype: IntstrIntOrString
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """
        Sets the target_port of this V1ServicePort.
        Number or name of the port to access on the pods targeted by the service. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. If this is a string, it will be looked up as a named port in the target Pod's container ports. If this is not specified, the value of the 'port' field is used (an identity map). This field is ignored for services with clusterIP=None, and should be omitted or set equal to the 'port' field. More info: http://kubernetes.io/docs/user-guide/services#defining-a-service

        :param target_port: The target_port of this V1ServicePort.
        :type: IntstrIntOrString
        """

        self._target_port = target_port

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
