#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []
  
  #Properties
  @property #Getter method
  def discount(self):
    return self._discount

  @discount.setter # Setter method
  def discount(self, discount_value):
    if isinstance(discount_value, (int, float)) and discount_value >= 0 and discount_value <= 100:
      self._discount = discount_value
    else:
      print("Not valid discount")

  # Methods
  def add_item(self, item, price, quantity=1):
    total_price = price * quantity
    self.total = self.total + total_price
    self.items.append(item)

    transaction_dictionary = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(transaction_dictionary)

  def apply_discount(self):
    if len(self.previous_transactions) < 1:
      print("There is no discount to apply.")
      return
    else:
      discount_value = (self.discount / 100) * self.total

      final_amount = self.total - discount_value

      # Ensuring that price(total) and items reflect correctly.
      last_index = len(self.previous_transactions) - 1
      last_transaction = self.previous_transactions[last_index]
      last_price = last_transaction['price']

      #Adjusting the total
      self.total = self.total - last_price

      #Adjusting the items array
      if last_transaction['item'] in self.items:
        self.items.remove(last_transaction['item'])

    return final_amount
  
  def void_last_transaction(self):
    if len(self.previous_transactions) > 1:
      self.previous_transactions.pop()

      # Ensuring that price(total) and items reflect correctly.
      last_index = len(self.previous_transactions) - 1
      last_transaction = self.previous_transactions[last_index]
      last_price = last_transaction['price']

      #Adjusting the total
      self.total = self.total - last_price

      #Adjusting the items array
      if last_transaction['item'] in self.items:
        self.items.remove(last_transaction['item'])
    else:
      print("There is no transaction to void.")
  

