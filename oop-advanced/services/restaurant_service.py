from models.restaurant import Restaurant
from models.evaluation import Evaluation
from models.menu.dish import Dish
from models.menu.drink import Drink

def create_restaurant():
    restaurant_name = input("Nome do restaurante: ")
    restaurant_category = input("Categoria do restaurante: ")
    Restaurant(restaurant_name, restaurant_category)

def find_all_restaurants():
    if Restaurant.hasnt_restaurants():
        print("Nenhum restaurante foi cadastrado")
    else:
        print_restaurants()

def find_restaurant():
    if Restaurant.hasnt_restaurants():
        print("Nenhum restaurante foi cadastrado")
        return
    print("\nRestaurantes cadastrados: ")
    print_restaurants()
    print("\n")
    chosen_restaurant_name = input("Qual o nome do restaurante a ser alterado? ")
    found_restaurant = None
    for restaurant in Restaurant.get_restaurants():
        if chosen_restaurant_name == restaurant.name:
            found_restaurant = restaurant
    return found_restaurant

def update_restaurant_status():
    found_restaurant = find_restaurant()
    if found_restaurant != None:
        found_restaurant.update_status()
    else:
        print("\nO Restaurante não foi encontrado")

def evaluate_restaurant():
    found_restaurant = find_restaurant()
    if found_restaurant == None:
        print("\nO Restaurante não foi encontrado")
        return
    print("\n")
    client_name = input("Qual o nome do cliente que realizou/realizará a avaliação? ")
    evaluation_score = None
    try:
        evaluation_score = int(input("Qual a nota, em número inteiro, do restaurante? "))
    except:
        print("A nota deve ser um valor inteiro")
        return
    found_restaurant.add_evaluation(Evaluation(client_name, evaluation_score))

def add_menu_item():
    found_restaurant = find_restaurant()
    if found_restaurant == None:
        print("\nO Restaurante não foi encontrado")
        return
    print("\n")
    menu_item_name = input("Nome do item do menu: ")
    menu_item_price = None
    try:
        menu_item_price = float(input("Preço do item do menu: "))
    except:
        print("O preço deve ser um valor numérico")
        return
    menu_item_description = input("Descrição do item do menu: ")
    menu_item_type = input("Tipo do item do menu (Prato ou Bebida): ")
    new_menu_item = None
    if menu_item_type == "Prato":
        try: 
            menu_item_volume = float(input("Volume do prato: "))
        except:
            print("O volume deve ser um valor numérico")
            return
        new_menu_item = Dish(menu_item_name, menu_item_price, menu_item_description, menu_item_volume)
    elif menu_item_type == "Bebida":
        try: 
            menu_item_volume = float(input("Volume do prato: "))
        except:
            print("O volume deve ser um valor numérico")
            return
        new_menu_item = Drink(menu_item_name, menu_item_price, menu_item_description, menu_item_volume)
    else:
        print("Tipo de item do menu inválido")
        return
    found_restaurant.add_menu_item(new_menu_item)

def print_restaurant_menu():
    found_restaurant = find_restaurant()
    if found_restaurant == None:
        print("\nO Restaurante não foi encontrado")
        return
    print("\n")
    print("Menu do restaurante: ")
    for i, menu_item in enumerate(found_restaurant.menu_items, 1):
        print(f'{i} - {menu_item}')
    print("\n")

def print_restaurants():
    for restaurant in Restaurant.get_restaurants():
        print(restaurant)

def print_restaurant_evaluations():
    found_restaurant = find_restaurant()
    if found_restaurant == None:
        print("\nO Restaurante não foi encontrado")
        return
    print("\n")
    for evaluation in found_restaurant.evaluations:
        print(evaluation)
    print("\n")