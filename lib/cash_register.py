#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount, total=0, items=[], previous_transactions=0):
    self.discount = discount
    self.total = total
    self.items = items
    self.previous_transactions = previous_transactions

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(item)
    self.previous_transactions = price * quantity

  def apply_discount(self):    
    if self.discount > 0:
      self.total = self.total * (100 - self.discount) / 100
      return f"After the discount, the total comes to ${int(self.total)}."
    else:
      return "There is no discount to apply."
    
  def void_last_transaction(self):
    self.total -= self.previous_transactions
    self.previous_transactions = 0
    if self.total > 0:
      return self.total
    else:
      print("There is no transaction void")