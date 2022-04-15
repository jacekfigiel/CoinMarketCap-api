from crypto import Crypto
import json


def parse():
    file = open('test_data.json')
    data = json.load(file)
    result = []
    for i in data['data']:
        c = Crypto(i['name'], i['symbol'], i['quote']["USD"]["price"],
                   i['quote']["USD"]["percent_change_24h"],
                   i['quote']["USD"]["percent_change_7d"],
                   i['quote']["USD"]["market_cap"],
                   i['quote']["USD"]["volume_24h"], i["circulating_supply"])
        result.append(c)
    return result

