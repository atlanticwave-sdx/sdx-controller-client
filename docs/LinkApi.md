# swagger_client.LinkApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-Controller/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_link**](LinkApi.md#get_link) | **GET** /link | get an existing link

# **get_link**
> get_link()

get an existing link

ID of the link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkApi()

try:
    # get an existing link
    api_instance.get_link()
except ApiException as e:
    print("Exception when calling LinkApi->get_link: %s\n" % e)
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

