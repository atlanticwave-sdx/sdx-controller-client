# swagger_client.ConnectionApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-Controller/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connection/{connection_id} | Delete connection order by ID
[**getconnection_by_id**](ConnectionApi.md#getconnection_by_id) | **GET** /connection/{connection_id} | Find connection by ID
[**getconnections**](ConnectionApi.md#getconnections) | **GET** /connections | List all connections
[**place_connection**](ConnectionApi.md#place_connection) | **POST** /connection | Place an connection request from the SDX-Controller

# **delete_connection**
> delete_connection(connection_id)

Delete connection order by ID

delete a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the connection that needs to be deleted

try:
    # Delete connection order by ID
    api_instance.delete_connection(connection_id)
except ApiException as e:
    print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**str**](.md)| ID of the connection that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getconnection_by_id**
> Connection getconnection_by_id(connection_id)

Find connection by ID

connection details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of connection that needs to be fetched

try:
    # Find connection by ID
    api_response = api_instance.getconnection_by_id(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->getconnection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | [**str**](.md)| ID of connection that needs to be fetched | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getconnections**
> list[Connection] getconnections()

List all connections

connection details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()

try:
    # List all connections
    api_response = api_instance.getconnections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->getconnections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Connection]**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_connection**
> Connection place_connection(body)

Place an connection request from the SDX-Controller

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.ConnectionBody() # ConnectionBody | order placed for creating a connection

try:
    # Place an connection request from the SDX-Controller
    api_response = api_instance.place_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->place_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionBody**](ConnectionBody.md)| order placed for creating a connection | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

