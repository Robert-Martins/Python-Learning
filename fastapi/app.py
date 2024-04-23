from fastapi import FastAPI, Query
import requests # type: ignore

URL = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

def handle_valid_restaurants_response(restaurant, response_data):
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
    return restaurant_data if restaurant is None or restaurant not in restaurant_data else restaurant_data[restaurant]

def get_restaurants_data(restaurant):
    response = requests.get(URL)

    if response.status_code == 200:
        return handle_valid_restaurants_response(restaurant, response.json())
    print(f"Erro ao acessar API: {response.status_code}")
    return None

app = FastAPI()

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/restaurants/")
def get_restaurants(restaurant: str = Query(None)):
    restaurants_data = get_restaurants_data(restaurant)
    if restaurants_data is None:
        return {"error": "Dados não encontrados"}
    return restaurants_data