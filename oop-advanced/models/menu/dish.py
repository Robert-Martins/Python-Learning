from models.menu.restaurant_menu_item import RestaurantMenuItem

class Dish(RestaurantMenuItem):

    def __init__(self, name, price, description, weight):
        super().__init__(name, price, description)
        self._weight = weight

    def __str__(self):
        return f'Bebida {self._name} por R$ {self._price} - {self._description} - Peso: {self._weight}'
    
    def apply_discount(self):
        self._price -= self._price * 0.25