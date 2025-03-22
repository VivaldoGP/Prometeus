from prometeus.prometeus import CopernicusAPI
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()

def test_open_node():
    username = getenv('cdse_username')
    password = getenv('cdse_password')
    api = CopernicusAPI(username, password)
    token = api.auth()
    headers = {"Authorization": f"Bearer {token}"}
    session = requests.Session()
    session.headers.update(headers)
    url = "https://zipper.dataspace.copernicus.eu/odata/v1/Products%28654968ae-65a3-4377-b9af-35a3d2642cad%29/Nodes%28S2B_MSIL2A_20250301T170129_N0511_R069_T14QML_20250301T215534.SAFE%29/Nodes%28DATASTRIP%29/Nodes%28DS_2BPS_20250301T215534_S20250301T171608%29/Nodes%28MTD_DS.xml%29/$value"
    response = session.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        print(response.text)  # Imprimir directamente el contenido XML
    else:
        print(f"Error al obtener el XML: {response.status_code}")
    assert response.status_code == 200