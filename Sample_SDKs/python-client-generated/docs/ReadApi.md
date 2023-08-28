# swagger_client.ReadApi

All URIs are relative to *http://localhost:3000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pet**](ReadApi.md#get_pet) | **GET** /pets/{id} | 
[**list_pets**](ReadApi.md#list_pets) | **GET** /pets | 

# **get_pet**
> InlineResponse200 get_pet(id)



Get a pet by its id

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
api_instance = swagger_client.ReadApi(swagger_client.ApiClient(configuration))
id = 1.2 # float | id of the pet to fetch

try:
    api_response = api_instance.get_pet(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->get_pet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| id of the pet to fetch | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pets**
> PetsList list_pets(max=max, order=order, offset=offset)



Lists all pets in the PetStore

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
api_instance = swagger_client.ReadApi(swagger_client.ApiClient(configuration))
max = 1.2 # float | Maximum number of items to return (optional)
order = 'order_example' # str | Sorting order (optional)
offset = 'offset_example' # str | offset id to get next page (optional)

try:
    api_response = api_instance.list_pets(max=max, order=order, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->list_pets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max** | **float**| Maximum number of items to return | [optional] 
 **order** | **str**| Sorting order | [optional] 
 **offset** | **str**| offset id to get next page | [optional] 

### Return type

[**PetsList**](PetsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

