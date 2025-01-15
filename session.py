from settings import api, secret
from pybit.unified_trading import HTTP

session = HTTP(
    api_key=api,
    api_secret=secret
)