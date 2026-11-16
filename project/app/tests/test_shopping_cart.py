from models.shopping_cart import ShoppingCart

class TestShoppingCart:
    def test_add_item(self):
        cart = ShoppingCart()

        cart.add_item("Apple", 3, 2)

        assert cart.items == [{
            "name": "Apple",
            "price": 3,
            "quantity": 2
        }]

    def test_remove_item(self):
        cart = ShoppingCart()

        cart.add_item("Apple", 3, 2)
        cart.remove_item("Apple")

        assert cart.items == []

    def test_add_same_item(self):
        cart = ShoppingCart()

        cart.add_item("Apple", 3, 2)
        cart.add_item("Apple", 3, 2)

        assert len(cart.items) == 1

