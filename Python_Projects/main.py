import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fd94545a707324db452ad28b6166ed66'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_new_name = {
    "pokemon_id": "330743",
    "name": "Holly",
    "photo_id": 2
}

body_in_pockeball = {
    "pokemon_id": "330650"
}

response_create = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create)
print(response_create.text)

response_new_name = requests.put(url = f'{URL}/pokemons' , headers = HEADER, json = body_new_name)
print(response_new_name.text)

response_in_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball' , headers = HEADER, json = body_in_pockeball)
print(response_in_pockeball.text)