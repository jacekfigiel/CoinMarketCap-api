from crypto import Crypto
from json_parser import parse


class FindTheWrightCrypto:

    def __init__(self):
        self.cryptos = parse()

    def find_crypto(self):
        ask = input("Give a symbol of crypto:\n").upper()
        for x in self.cryptos:
            if ask in x.symbol:
                print(x[ask])
            elif ask not in x.symbol:
                print(f"No crypro with name {ask}")



FindTheWrightCrypto().find_crypto()
