import os # biblioteca built-in para consumo do OS

restaurants = []

DEFAULT_RESTAURANT_STATUS = False

def shutdown():
    os.system('cls') # limpa o terminal
    # s.system('clear') no mac
    print("Finalizando o App")

def create_restaurant():
    option_chosen("Cadastro de novo Restaurante")
    restaurant_name = input("Nome do restaurante: ")
    restaurants.append({
        'name': restaurant_name,
        'active': DEFAULT_RESTAURANT_STATUS
    })
    back_to_menu()

def find_all_restaurants():
    option_chosen("Restaurantes cadastrados:")
    if len(restaurants) == 0:
        print("Nenhum restaurante foi cadastrado")
    else:
        print_restaurants()
    back_to_menu()

def update_restaurant_status():
    option_chosen("Alterar status de restaurante")
    if len(restaurants) == 0:
        print("Nenhum restaurante foi cadastrado")
        back_to_menu()
    print("\nRestaurantes cadastrados: ")
    print_restaurants()
    print("\n")
    chosen_restaurant_name = input("Qual o nome do restaurante que terá o status alterado? ")
    found_restaurant = None
    for restaurant in restaurants:
        if chosen_restaurant_name == restaurant['name']:
            found_restaurant = restaurant
    if found_restaurant != None:
        found_restaurant['active'] = not found_restaurant['active']
        print_restaurant(found_restaurant)
    else:
        print("\nO Restaurante não foi encontrado")
    back_to_menu()

def print_restaurant(restaurant):
    print(f" - {restaurant['name']} -> {'Ativo' if restaurant['active'] else 'Inativo'}")

def print_restaurants():
    for restaurant in restaurants:
        print_restaurant(restaurant)

def print_app_name():
    print("""
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░   
    """)

def print_menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar status do restaurante")
    print("\n0. Encerrar programa\n")

def choose_option():
    try:
        handle_valid_option()
    except:
        handle_invalid_option()
        
def option_chosen(title):
    os.system("cls")
    print(f"\n{title}\n")

def handle_valid_option():
    chosen_option = int(input("Escolha uma opção: "))
    print(f'\nOpção escolhida: {chosen_option}\n')
    # chosen_option = int(chosen_option)
    handle_chosen_option(chosen_option)

def handle_invalid_option():
    option_chosen("Opção inválida")
    back_to_menu()

def handle_chosen_option(option):
    match option:
        case 1:
            create_restaurant()
        case 2:
            find_all_restaurants()
        case 3:
            update_restaurant_status()
        case 0:
            shutdown()
        case _:
            handle_invalid_option()

def back_to_menu():
    print("\n\n")
    menu_interaction()

def menu_interaction():
    print_menu()
    choose_option()

def main():
    print_app_name()
    menu_interaction()

if __name__ == "__main__":
    main()