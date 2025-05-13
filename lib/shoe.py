#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand=brand
        self.size=size
        self.condition= None

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if not isinstance(size,int):
            print("size must be an integer")
            self._size="Invalid size"
        else:
            self._size=size

        


