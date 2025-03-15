from urllib.parse import quote, urlencode

def test_urlparse():
    string_obj = 'cloudCover=[0,10]'
    assert quote(string_obj, safe='=') == 'cloudCover=%5B0%2C10%5D'

def test_urlencode(cloud_cover: int = 10):
    params = {
        "platform": "S2A",
        "maxRecords": 5,
        "cloudCover": f"[0,{cloud_cover}]",
        "startDate": "2021-07-01T00:00:00Z",
        "completionDate": "2021-07-31T23:59:59Z"
    }
    test_url = "https://catalogue.dataspace.copernicus.eu/resto/api/collections/Sentinel2/search.json?"
    new_url = f"{test_url}{urlencode(params, safe=":")}"
    #assert urlencode(params, safe=',[]') == 'platform=S2A&maxRecords=5&cloudCover=[0,10]'
    print(new_url)
    assert new_url == "https://catalogue.dataspace.copernicus.eu/resto/api/collections/Sentinel2/search.json?platform=S2A&maxRecords=5&cloudCover=%5B0%2C10%5D&startDate=2021-07-01T00:00:00Z&completionDate=2021-07-31T23:59:59Z"