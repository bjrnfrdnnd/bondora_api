from __future__ import print_function
import time
import bondora_api
from bondora_api.rest import ApiException
from pprint import pprint

config = bondora_api.Configuration()
token = 'your_api_token_here'
config.api_key['Authorization'] = token
config.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bondora_api.AccountApi(bondora_api.ApiClient(config))
api_response = api_instance.account_get_balance()
pprint(api_response)

pass