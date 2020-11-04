import requests

import config


async def get_data():
    return requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
        params=dict(id=1),
        headers={"X-CMC_PRO_API_KEY": config.API_KEY, "Accept": "application/json"},
    )
