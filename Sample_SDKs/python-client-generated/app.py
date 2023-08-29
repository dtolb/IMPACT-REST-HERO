from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'abc123456'

read_api = swagger_client.ReadApi(swagger_client.ApiClient(configuration))
write_api = swagger_client.WriteApi(swagger_client.ApiClient(configuration))
id = 1

YOUR_PETS_NAME="Dolph"
YOUR_UPDATED_PETS_NAME="Molly"

try:
    createPetRequest = swagger_client.models.CreatePetRequest(name=YOUR_PETS_NAME, species="dog")
    api_response = write_api.create_pet(createPetRequest)
    print("--Created Pet--")
    pprint(api_response)
    id = api_response.id
except ApiException as e:
    print("Exception when calling WriteAPI->create_pet: %s\n" % e)

try:
    api_response = read_api.get_pet(id)
    print("--Get Pet--")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->get_pet: %s\n" % e)

try:
    updatePetRequest = swagger_client.models.UpdatePetRequest(name=YOUR_UPDATED_PETS_NAME)
    api_response = write_api.update_pet(id=id, body=updatePetRequest)
    print("--Update Pet--")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WriteAPI->update_pet: %s\n" % e)

try:
    api_response = read_api.list_pets()
    print("--List Pets--")
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReadApi->list_pets: %s\n" % e)

