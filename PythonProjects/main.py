import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c011723c21df452239c5b662e7a2008'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "Буля",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "204280",
    "name": "Котозавр",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "204280"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_pokeball = requests.post(f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)