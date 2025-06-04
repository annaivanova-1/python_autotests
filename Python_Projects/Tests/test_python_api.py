import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fd94545a707324db452ad28b6166ed66'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '34198'

def test_get_trainers_status_code_200():
    response = requests.get(url = f'{URL}/trainers/' , params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(url=f'{URL}/trainers/', params={'trainer_id': TRAINER_ID})
    assert response.json()["data"][0]["trainer_name"] == 'Зевс'