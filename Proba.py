class Order:
    product = "Milk"
    amount = 0

    def set_amount(self, value):
        if value < 0:
            raise ValueError()
        self._amount = value

order = Order()
order.set_amount(10)
print(order.set_amount, order.product)