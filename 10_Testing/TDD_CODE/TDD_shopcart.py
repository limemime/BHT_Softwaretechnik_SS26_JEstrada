import unittest

class TestShoppingCart(unittest.TestCase):
    def test_empty_cart_has_zero_total(self):
        cart = ShoppingCart()
        self.assertEqual(cart.get_total(), 0)

if __name__ == "__main__":
    unittest.main()
