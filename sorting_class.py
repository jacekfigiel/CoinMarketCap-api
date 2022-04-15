from crypto import Crypto
from json_parser import parse


class SortingCrypto:

    sorted_crypto: list[Crypto]

    def __init__(self):
        self.c = parse()

    @property
    def sorting_cro_highest_price(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.price, reverse=True)
        return self.sorted_crypto

    def sorting_cro_lowest_price(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.price)
        return self.sorted_crypto

    def sort_cro_top_gain_24h(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.percent_change_24h, reverse=True)
        return self.sorted_crypto

    def sort_cro_top_losses_24h(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.percent_change_24h)
        return self.sorted_crypto

    def sort_cro_top_gain_7d(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.percent_change_7d, reverse=True)
        return self.sorted_crypto

    def sort_crypto_top_losses_7d(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.percent_change_7d)
        return self.sorted_crypto

    def sort_crypto_top_market_cap(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.market_cap, reverse=True)
        return self.sorted_crypto

    def sort_crypto_bottom_market_cap(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.market_cap)
        return self.sorted_crypto

    def sort_crypto_top_volume_24h(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.volume_24h, reverse=True)
        return self.sorted_crypto

    def sort_crypto_bottom_volume_24h(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.volume_24h)
        return self.sorted_crypto

    def sort_crypto_the_most_circulating_supply(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.circulating_supply, reverse=True)
        return self.sorted_crypto

    def sort_crypto_least_circulating_supply(self):
        self.sorted_crypto = sorted(self.c, key=lambda x: x.circulating_supply)
        return self.sorted_crypto
