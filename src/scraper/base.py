from settings import SCRAPER_API_KEY, SCRAPER_API_URL

class Scraper:
    def __init__(
        self: Scraper,
        base_url: str | None = SCRAPER_API_URL,
        api_key: str | None = SCRAPER_API_KEY
        ):
        self.base_url = base_url
        self.api_key = api_key
    
    def _validate_config(self):
        if not self.api_key:
            raise ValueError("`api_key` is required to use `Scraper` object.")
        if not self.base_url:
            raise ValueError("`base_url` is required to use `Scraper` object.")
        
    def scrape(self):
        self._validate_config()
        