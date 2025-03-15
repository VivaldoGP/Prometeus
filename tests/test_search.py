from prometeus.search import get_collections
from prometeus.prometeus import CopernicusAPI
import requests


def test_search_collections():
    api = CopernicusAPI()
    products = api.search(mission_id='Sentinel2', max_records=20, cloud_cover=20, start_date="2025-03-09", end_date="2025-03-14")
    print(products.json())
    assert products is not None

def test_os_url(start_date: str = "2025-03-09", end_date: str = "2025-03-14"):
    url = f"https://catalogue.dataspace.copernicus.eu/resto/api/collections/Sentinel2/search.json?startDate={start_date}&completionDate={end_date}&sortParam=startDate&maxRecords=20"
    response = requests.get(url).json()
    assert response is not None
    print(response)