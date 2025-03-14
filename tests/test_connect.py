import pytest
from prometeus.connect import get_access_token
from dotenv import load_dotenv
from os import getenv
from prometeus.prometeus import CopernicusAPI

load_dotenv()

def test_get_access_token():

    username = getenv('cdse_username')
    password = getenv('cdse_password')
    token = get_access_token(username, password)
    print(token)
    assert token is not None


def test_connect():
    username = getenv('cdse_username')
    password = getenv('cdse_password')
    api = CopernicusAPI(username, password)
    token = api.auth()
    assert token is not None