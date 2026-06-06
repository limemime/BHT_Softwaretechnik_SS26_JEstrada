import unittest

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
        print(f"Items in cart: {self.items}")

    def add_items(self, item_list):
        self.items.extend(item_list)
        print(f"Items in cart: {self.items}")

    def get_total(self):
        return sum(item[1] for item in self.items)

    def get_quantity(self, name):
        return sum(1 for item in self.items if item[0] == name)

class TestShoppingCart(unittest.TestCase):
    def test_empty_cart_has_zero_total(self):
        cart = ShoppingCart()
        self.assertEqual(cart.get_total(), 0)

    def test_add_item_increase_total(self):
        cart = ShoppingCart()
        cart.add_item("Apple", 1.5)
        self.assertEqual(cart.get_total(), 1.5)

    def test_add_multiple_items_sums_total(self):
        cart = ShoppingCart()
        cart.add_items([("Apple", 1.5), ("Banana", 2.0), ("Orange", 3.0)])
        self.assertEqual(cart.get_total(), 6.5)

    def test_get_quantity_of_item(self):
        cart = ShoppingCart()
        cart.add_items([("Apple", 1.5), ("Apple", 1.5), ("Banana", 2.0)])
        self.assertEqual(cart.get_quantity("Apple"), 2)
        self.assertEqual(cart.get_quantity("Banana"), 1)
        self.assertEqual(cart.get_quantity("Orange"), 0)

    def test_remove_item(self):
        cart = ShoppingCart()
        cart.add_items([("Apple", 1.5), ("Banana", 2.0)])
        cart.remove_item("Apple")
        self.assertEqual(cart.get_quantity("Apple"), 0)
        self.assertEqual(cart.get_total(), 2.0)

if __name__ == "__main__":
    unittest.main()
