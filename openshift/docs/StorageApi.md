# openshift.client.StorageApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_api_group**](StorageApi.md#get_storage_api_group) | **GET** /apis/storage.k8s.io/ | 


# **get_storage_api_group**
> UnversionedAPIGroup get_storage_api_group()



get information of a group

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.StorageApi()

try: 
    api_response = api_instance.get_storage_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageApi->get_storage_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIGroup**](UnversionedAPIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

