#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, price):
        self.brand = brand
        self._size = size
        self._price = price
        self._condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        self._size = new_size

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def repair(self):
        self._condition = "New"
        print("The shoe has been repaired.")
