from prometeus.connect import get_access_token
from requests import get
from datetime import datetime
from datetime import timedelta
from urllib.parse import urlencode, quote


class CopernicusAPI:
    def __init__(
            self,
            username=None,
            password=None,
            token_url="https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
    ):
        self.username = username
        self.password = password
        self.token_url = token_url
        self.access_token = None
        self.catalog_url = "https://catalogue.dataspace.copernicus.eu/resto/api/collections"

    def auth(self):
        if self.username and self.password and not self.access_token:
            self.access_token = get_access_token(
                username=self.username,
                password=self.password,
                token_url=self.token_url,
            )
            return self.access_token

    def search(self,
               mission_id: str = "Sentinel2",
               platform: str = "S2A",
               max_records: int = 5,
               start_date: str = None,
               end_date: str = None,
               cloud_cover: int = 10):

        params = {
            "platform": platform,
            "maxRecords": max_records
        }

        if end_date:
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
            params["completionDate"] = end_date_dt.strftime("%Y-%m-%d")

            if not start_date:
                start_date = (end_date_dt - timedelta(days=5)).strftime("%Y-%m-%d")

        if start_date:
            params["startDate"] = start_date

        #self.catalog_url = f"{self.catalog_url}/{mission_id}/search.json?cloudCover=[0,{cloud_cover}]&{urlencode(params, safe='[]')}"
        #print(self.catalog_url)
        self.catalog_url = f"{self.catalog_url}/{mission_id}/search.json?startDate={start_date}&completionDate={end_date}&platform=S2C&maxRecords={max_records}"
        print(self.catalog_url)
        response = get(self.catalog_url).json()
        return response
