import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='3445a1c6131e69ee9cc93dde726558b8'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
  "name": "Terminator11",
  "photo_id": 1002
}

response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json= body_create)
print(response_create.text)

message=response_create.json()['message']
print(message)

body_change = {
  "pokemon_id": "75236",
  "name": "Terminator999",
  "photo_id": 2
}

response_change=requests.put(url=f'{URL}/pokemons', headers=HEADER, json= body_change)
print(response_change.text)

message=response_change.json()['message']
print(message)

body_pokeball = {
  "pokemon_id": "75236"
}

response_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_pokeball)
print(response_pokeball.text)

message=response_pokeball.json()['message']
print(message)