class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        for i in self.items:
            if i["name"] == name:
                i["price"] = price
                i["quantity"] += quantity
                return

        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity,
        })

    def remove_item(self, name):
        for i in self.items:
            if i["name"] == name:
                self.items.remove(i)
                return
