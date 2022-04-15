from crypto import Crypto
from json_parser import parse


class FindTheWrightCrypto:
    sorted_crypto: list[Crypto]

    def __init__(self):
        self.cryptos = parse()

    def find_crypto(self):
        x = input("Give a crypto name:")
        for x in self.cryptos:# nie wiem jak ugrysc rozpakowywanie listy
            if x.symbol in x.symbol:
                print(x.symbol)



