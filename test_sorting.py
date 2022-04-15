import unittest
from sorting_class import SortingCrypto


class TestSortingCrypto(unittest.TestCase):

    def test_sorting_highest(self):
        self.cryptos = SortingCrypto().sorting_cro_highest_price
        self.assertEqual(self.cryptos[0].name, "Bitcoin")
        self.assertEqual(self.cryptos[1].name, "Wrapped Bitcoin")
        self.assertEqual(self.cryptos[2].name, "yearn.finance")

    def test_sorting_lowest(self):
        self.cryptos = SortingCrypto().sorting_cro_lowest_price()
        self.assertEqual(self.cryptos[0].name, "Shiba Inu")
        self.assertEqual(self.cryptos[1].name, "eCash")
        self.assertEqual(self.cryptos[2].name, "BitTorrent-New")

    def test_top_gain_24h(self):
        self.cryptos = SortingCrypto().sort_cro_top_gain_24h()
        self.assertEqual(self.cryptos[0].percent_change_24h, 19.76)
        self.assertEqual(self.cryptos[1].percent_change_24h, 18.65)
        self.assertEqual(self.cryptos[2].percent_change_24h, 9.27)

    def test_top_losses_24h(self):
        self.cryptos = SortingCrypto().sort_cro_top_losses_24h()
        self.assertEqual(self.cryptos[0].percent_change_24h, -11.13)
        self.assertEqual(self.cryptos[1].percent_change_24h, -6.58)
        self.assertEqual(self.cryptos[2].percent_change_24h, -5.33)

    def test_top_gain_7d(self):
        self.cryptos = SortingCrypto().sort_cro_top_gain_7d()
        self.assertEqual(self.cryptos[0].percent_change_7d, 235.88)
        self.assertEqual(self.cryptos[1].percent_change_7d, 89.53)
        self.assertEqual(self.cryptos[2].percent_change_7d, 67.17)

    def test_top_losses_7d(self):
        self.cryptos = SortingCrypto().sort_crypto_top_losses_7d()
        self.assertEqual(self.cryptos[0].percent_change_7d, -10.84)
        self.assertEqual(self.cryptos[1].percent_change_7d, -9.3)
        self.assertEqual(self.cryptos[2].percent_change_7d, -7.08)

    def test_top_market_cap(self):
        self.cryptos = SortingCrypto().sort_crypto_top_market_cap()
        self.assertEqual(self.cryptos[0].name, "Bitcoin")
        self.assertEqual(self.cryptos[1].name, "Ethereum")
        self.assertEqual(self.cryptos[2].name, "Tether")

    def test_bottom_market_cap(self):
        self.cryptos = SortingCrypto().sort_crypto_bottom_market_cap()
        self.assertEqual(self.cryptos[0].name, "yearn.finance")
        self.assertEqual(self.cryptos[1].name, "Qtum")
        self.assertEqual(self.cryptos[2].name, "Decred")

    def test_top_volume_24h(self):
        self.cryptos = SortingCrypto().sort_crypto_top_volume_24h()
        self.assertEqual(self.cryptos[0].name, "Tether")
        self.assertEqual(self.cryptos[1].name, "Bitcoin")
        self.assertEqual(self.cryptos[2].name, "Ethereum")

    def test_bottom_volume_24h(self):
        self.cryptos = SortingCrypto().sort_crypto_bottom_volume_24h()
        self.assertEqual(self.cryptos[0].name, "Decred")
        self.assertEqual(self.cryptos[1].name, "Pax Dollar")
        self.assertEqual(self.cryptos[2].name, "UNUS SED LEO")

    def test_the_most_supply(self):
        self.cryptos = SortingCrypto().sort_crypto_the_most_circulating_supply()
        self.assertEqual(self.cryptos[0].name, "BitTorrent-New")
        self.assertEqual(self.cryptos[1].name, "Shiba Inu")
        self.assertEqual(self.cryptos[2].name, "eCash")

    def test_the_least_supply(self):
        self.cryptos = SortingCrypto().sort_crypto_least_circulating_supply()
        self.assertEqual(self.cryptos[0].name, "yearn.finance")
        self.assertEqual(self.cryptos[1].name, "Wrapped Bitcoin")
        self.assertEqual(self.cryptos[2].name, "Maker")


if __name__ == '__main__':
    unittest.main()
