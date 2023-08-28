# swagger_client.WriteApi

All URIs are relative to *http://localhost:3000/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pet**](WriteApi.md#create_pet) | **POST** /pets | 
[**update_pet**](WriteApi.md#update_pet) | **PUT** /pets/{id} | 

# **create_pet**
> Pet create_pet(body)



Create a new pet with its adorable name

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
api_instance = swagger_client.WriteApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreatePetRequest() # CreatePetRequest | the information to create the pet

try:
    api_response = api_instance.create_pet(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WriteApi->create_pet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePetRequest**](CreatePetRequest.md)| the information to create the pet | 

### Return type

[**Pet**](Pet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pet**
> InlineResponse200 update_pet(body, id)



Update the pet information by its id

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
api_instance = swagger_client.WriteApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdatePetRequest() # UpdatePetRequest | the information to update the Pet
id = 1.2 # float | id of the pet to update

try:
    api_response = api_instance.update_pet(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WriteApi->update_pet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePetRequest**](UpdatePetRequest.md)| the information to update the Pet | 
 **id** | **float**| id of the pet to update | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

