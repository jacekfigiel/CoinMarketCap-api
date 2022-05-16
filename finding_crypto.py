from crypto import Crypto
from json_parser import parse


class FindTheWrightCrypto:

    def __init__(self):
        self.cryptos = parse()

    def find_crypto(self):
        found_crypto = FindTheWrightCrypto().iterate()
        if found_crypto:
            print(found_crypto)
        else:
            print("No crypto wit that name.")

    def iterate(self):
        ask = input("Give a symbol of crypto:\n")
        for x in self.cryptos:
            if ask.upper() == x.symbol:
                return x
            elif ask.title() == x.name:
                return x


FindTheWrightCrypto().find_crypto()
