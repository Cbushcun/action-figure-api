import requests

from src.config import SCRAPER_API_KEY, SCRAPER_API_URL

class Scraper:
    def __init__(
        self: Scraper,
        base_url: str | None = SCRAPER_API_URL,
        api_key: str | None = SCRAPER_API_KEY,
        output_formats: list[str] = ["html"]
        ):
        self._base_url = base_url
        self._api_key = api_key
        self._output_formats = output_formats
    
    def _validate_config(self):
        if not self._api_key:
            raise ValueError("`api_key` is required to use `Scraper` object.")
        if not self._base_url:
            raise ValueError("`base_url` is required to use `Scraper` object.")
        
    def scrape(self, url):
        self._validate_config()
        payload = {
            "url": url,
            "outputFormat": self._output_formats
        }
        headers = {
            "Content-Type": "application/json",
            "x-api-key": SCRAPER_API_KEY
        }
        if self._base_url:
            res = requests.post(self._base_url, json=payload, headers=headers)
        return res
        