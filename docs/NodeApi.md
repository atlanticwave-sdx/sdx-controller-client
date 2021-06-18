# swagger_client.NodeApi

All URIs are relative to *https://virtserver.swaggerhub.com/YufengXin/SDX-Controller/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node**](NodeApi.md#get_node) | **GET** /node | get an existing node

# **get_node**
> get_node()

get an existing node

ID of the node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()

try:
    # get an existing node
    api_instance.get_node()
except ApiException as e:
    print("Exception when calling NodeApi->get_node: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

