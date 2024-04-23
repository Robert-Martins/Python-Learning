import requests # type: ignore
import json

URL = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

def save_restaurant_data(restaurant_name, restaurant_data):
    file_name = f'{restaurant_name}.json'
    with open(file_name, 'w') as restaurant_file:
        json.dump(restaurant_data, restaurant_file, indent=4)

def save_restaurants_data(restaurants_data):
    for restaurant_name, items in restaurants_data.items():
        save_restaurant_data(restaurant_name, items)

def handle_valid_restaurants_response(response_data):
    restaurant_data = {}
    for item in response_data:
        restaurant_name = item['Company']
        if restaurant_name not in restaurant_data:
            restaurant_data[restaurant_name] = []
        restaurant_data[restaurant_name].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
    save_restaurants_data(restaurant_data)

def get_restaurants_data():
    response = requests.get(URL)

    if response.status_code == 200:
        handle_valid_restaurants_response(response.json())
    else:
        print(f"Erro ao acessar API: {response.status_code}")

if __name__ == '__main__':
    get_restaurants_data()