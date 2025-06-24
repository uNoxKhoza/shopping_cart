
import unittest
from shopping_cart import add_to_cart, calculate_total

class TestShoppingCart(unittest.TestCase):
    def test_add_to_cart(self):
        cart = {'foods': [], 'prices': []}
        updated_cart = add_to_cart("Apples", 10.0, cart)
        self.assertIn("Apples", updated_cart['foods'])
        self.assertIn(10.0, updated_cart['prices'])

    def test_calculate_total(self):
        prices = [10.0, 15.5, 5.5]
        self.assertEqual(calculate_total(prices), 31.0)

if __name__ == '__main__':
    unittest.main()
