import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def get_total(self):
        return 0

class TestShoppingCart(unittest.TestCase):
    def test_empty_cart_has_zero_total(self):
        cart = ShoppingCart()
        self.assertEqual(cart.get_total(), 0)

    def test_add_item_increase_total(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        self.assertEqual(cart.get_total(), 1.5)

if __name__ == "__main__":
    unittest.main()
