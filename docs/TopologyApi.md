# swagger_client.TopologyApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-Controller/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_topology**](TopologyApi.md#get_topology) | **GET** /topology | get an existing topology
[**get_topologyby_version**](TopologyApi.md#get_topologyby_version) | **GET** /topology/{version} | Find topology by version
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

# **get_topologyby_version**
> Topology get_topologyby_version(topology_id, version)

Find topology by version

Returns a single topology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
topology_id = 789 # int | ID of topology to return
version = 789 # int | version of topology to return

try:
    # Find topology by version
    api_response = api_instance.get_topologyby_version(topology_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topologyby_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to return | 
 **version** | **int**| version of topology to return | 

### Return type

[**Topology**](Topology.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
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

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

