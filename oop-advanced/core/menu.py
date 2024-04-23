from services.restaurant_service import *
import os

def shutdown():
    os.system('cls') # limpa o terminal
    # s.system('clear') no mac
    print("Finalizando o App")

def perform_restaurant_creation():
    option_chosen("Cadastro de novo Restaurante")
    create_restaurant()
    back_to_menu()

def perform_restaurants_listing():
    option_chosen("Restaurantes cadastrados:")
    find_all_restaurants()
    back_to_menu()

def perform_restaurant_status_update():
    option_chosen("Alterar status de Restaurante")
    update_restaurant_status()
    back_to_menu()

def perform_restaurant_evaluation():
    option_chosen("Avaliar Restaurante")
    evaluate_restaurant()
    back_to_menu()

def perform_restaurant_evaluations_listing():
    option_chosen("Visualizar avaliações de um Restaurante")
    print_restaurant_evaluations()
    back_to_menu()

def perform_add_menu_item():
    option_chosen("Adicionar item ao cardápio de um Restaurante")
    add_menu_item()
    back_to_menu()

def perform_list_menu_items():
    option_chosen("Listar itens do cardápio de um Restaurante")
    print_restaurant_menu()
    back_to_menu()

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
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Alterar status de um Restaurante")
    print("4. Avaliar Restaurante")
    print("5. Visualizar avaliações de um Restaurante")
    print("6. Adicionar item ao cardápio de um Restaurante")
    print("7. Listar itens do cardápio de um Restaurante")
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
            perform_restaurant_creation()
        case 2:
            perform_restaurants_listing()
        case 3:
            perform_restaurant_status_update()
        case 4:
            perform_restaurant_evaluation()
        case 5:
            perform_restaurant_evaluations_listing()
        case 6:
            perform_add_menu_item()
        case 7:
            perform_list_menu_items()
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

def start_app():
    print_app_name()
    menu_interaction()