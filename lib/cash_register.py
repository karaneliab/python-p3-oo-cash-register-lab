#!/usr/bin/env python3
class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def reset_register_totals(self):
        self.total = 0

    def add_item(self, item_name, price, quantity=1):
        for _ in range(quantity):
            self.items.append((item_name, price))
            self.total += price

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1]
        else:
            print("No items to void.")

    def get_all_items(self):
        return self.items

    def get_total(self):
        return self.total
        


