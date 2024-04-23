from models.menu.restaurant_menu_item import RestaurantMenuItem

class Drink(RestaurantMenuItem):

    def __init__(self, name, price, description, volume):
        super().__init__(name, price, description)
        self._volume = volume

    def __str__(self):
        return f'Prato {self._name} por R$ {self._price} - {self._description} - Volume: {self._weight}'
    
    def apply_discount(self):
        self._price -= self._price * 0.05