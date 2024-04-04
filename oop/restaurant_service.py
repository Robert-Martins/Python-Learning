from restaurant import Restaurant
from evaluation import Evaluation

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