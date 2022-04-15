import unittest
from json_parser import parse


class TestParser(unittest.TestCase):

    def setUp(self):
        self.cryptos = parse()

    def test_parse(self):
        self.assertEqual(self.cryptos[0].name, "Bitcoin")
        self.assertEqual(self.cryptos[0].symbol, "BTC")
        self.assertEqual(self.cryptos[0].price, 46391.46)
        self.assertEqual(self.cryptos[0].percent_change_24h, -0.36)
        self.assertEqual(self.cryptos[0].percent_change_7d, 3.95)
        self.assertEqual(self.cryptos[0].market_cap, 881501114888.2994)
        self.assertEqual(self.cryptos[0].volume_24h, 27930301049.69587)
        self.assertEqual(self.cryptos[0].circulating_supply, 19001368)

        self.assertEqual(self.cryptos[1].name, "Ethereum")
        self.assertEqual(self.cryptos[1].symbol, "ETH")
        self.assertEqual(self.cryptos[1].price, 3494.05)
        self.assertEqual(self.cryptos[1].percent_change_24h, 0.50)
        self.assertEqual(self.cryptos[1].percent_change_7d, 10.87)
        self.assertEqual(self.cryptos[1].market_cap, 420069284745.01465)
        self.assertEqual(self.cryptos[1].volume_24h, 18999000228.646347)
        self.assertEqual(self.cryptos[1].circulating_supply, 120224135.5615)

        self.assertEqual(self.cryptos[2].name, "Tether")
        self.assertEqual(self.cryptos[2].symbol, "USDT")
        self.assertEqual(self.cryptos[2].price, 1.00)
        self.assertEqual(self.cryptos[2].percent_change_24h, 0.00)
        self.assertEqual(self.cryptos[2].percent_change_7d, -0.00)
        self.assertEqual(self.cryptos[2].market_cap, 82334941611.00826)
        self.assertEqual(self.cryptos[2].volume_24h, 77510316743.36446)
        self.assertEqual(self.cryptos[2].circulating_supply, 82301930534.35547)


if __name__ == '__main__':
    unittest.main()
