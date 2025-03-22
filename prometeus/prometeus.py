from prometeus.connect import get_access_token
from requests import get
from datetime import datetime
from datetime import timedelta
from urllib.parse import urlencode
from utils.formats import to_iso_8601


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

    def auth(self) -> str | None:
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
        """
        params = {
            "platform": platform,
            "maxRecords": max_records,
            "cloudCover": f"[0,{cloud_cover}]",
            "startDate": to_iso_8601(start_date),
            "completionDate": to_iso_8601(end_date)
        }
        """
        params = self.query_params(start_date, end_date, max_records, cloud_cover, platform)
        print(params)

        self.catalog_url = f"{self.catalog_url}/{mission_id}/search.json?"
        self.catalog_url = f"{self.catalog_url}{urlencode(params, safe=':')}"
        #print(self.catalog_url)
        #self.catalog_url = f"{self.catalog_url}/{mission_id}/search.json?startDate={start_date}&completionDate={end_date}&platform=S2C&maxRecords={max_records}&cloudCover=[0,{cloud_cover}]"
        print(self.catalog_url)
        response = get(self.catalog_url).json()
        return response

    @staticmethod
    def query_params(start_date: str = None, end_date: str = None, max_records: int = 5, cloud_cover: int = 20,
                     platform: str = "S2A") -> dict:

        if end_date is None:
            raw_end_date = datetime.now()
            if start_date is None:
                raw_start_date = raw_end_date - timedelta(days=5)
                start_date = raw_start_date.replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
            end_date = raw_end_date.replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
        elif start_date is not None and end_date is not None:
            raw_start_date = datetime.strptime(start_date, "%Y-%m-%d")
            start_date = raw_start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
            raw_end_date = datetime.strptime(end_date, "%Y-%m-%d")
            end_date = raw_end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
            print(start_date, end_date)

        params = {
            "platform": platform,
            "maxRecords": max_records,
            "cloudCover": f"[0,{cloud_cover}]",
            "startDate": start_date,
            "completionDate": end_date
        }

        return params



