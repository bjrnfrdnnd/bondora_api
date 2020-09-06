from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

config = swagger_client.Configuration()
token = 'your_api_token_here'
config.api_key['Authorization'] = token
config.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AccountApi(swagger_client.ApiClient(config))
api_response = api_instance.account_get_balance()
pprint(api_response)

pass