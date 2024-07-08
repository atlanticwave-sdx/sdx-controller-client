# swagger_client.TopologyApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-Controller/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_topology**](TopologyApi.md#get_topology) | **GET** /topology | get an existing topology
[**get_topologyby_grenml**](TopologyApi.md#get_topologyby_grenml) | **GET** /topology/grenml | Get topology grenml
[**topology_version**](TopologyApi.md#topology_version) | **GET** /topology/version | Finds topology version

# **get_topology**
> str get_topology()

get an existing topology

ID of the topology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()

try:
    # get an existing topology
    api_response = api_instance.get_topology()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topologyby_grenml**
> str get_topologyby_grenml()

Get topology grenml

Returns a single topology by grenml

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()

try:
    # Get topology grenml
    api_response = api_instance.get_topologyby_grenml()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topologyby_grenml: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_version**
> Topology topology_version(topology_id)

Finds topology version

Topology version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()
topology_id = 'topology_id_example' # str | topology id

try:
    # Finds topology version
    api_response = api_instance.topology_version(topology_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->topology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **str**| topology id | 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

