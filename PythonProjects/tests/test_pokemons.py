import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6c011723c21df452239c5b662e7a2008'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '27865'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'LLL'

