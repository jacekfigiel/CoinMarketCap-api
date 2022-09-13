import unittest
from finding_crypto import *
from unittest import mock


class TestFindingCrypto(unittest.TestCase):

    def test_finding_crypto_by_symbol(self, mocked_input):
        self.cryptos = find_crypto
        mocked_input.side_effect = "ETH"
        self.assertEqual(self.cryptos, "ETH")


if __name__ == '__main__':
    unittest.main()
