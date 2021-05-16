from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
from my_secrets import api_key, api_secret
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = api_key,
    secret = api_secret
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
status = 'status' # str | List orders based on status
market = 'BTC_USDT' # str | Currency pair (optional)
# account = 'account_example' # str | Trading account (optional)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve running auto order list
    api_response = api_instance.list_spot_price_triggered_orders(status, market=market, account=account, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_spot_price_triggered_orders: %s\n" % e)
