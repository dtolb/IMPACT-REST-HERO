from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'abc123456'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ReadApi(swagger_client.ApiClient(configuration))
id = 1 # float | id of the pet to fetch

try:
    api_response = api_instance.get_pet(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->get_pet: %s\n" % e)

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'abc123456'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ReadApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.list_pets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->list_pets: %s\n" % e)