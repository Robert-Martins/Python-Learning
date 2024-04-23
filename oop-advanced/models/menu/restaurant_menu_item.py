from abc import ABC, abstractmethod

class RestaurantMenuItem:

    def __init__(self, name, price, description):
        self._name = name
        self._price = price
        self._description = description

    def __str__(self) -> str:
        return f'{self._name} por R$ {self._price} - {self._description}'
    
    @abstractmethod
    def apply_discount(self, discount):
        pass
    
