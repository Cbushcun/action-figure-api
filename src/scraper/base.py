import requests

from urllib.parse import urlsplit

class Scraper:
    def __init__(self: Scraper, base_url: object | None = None, timeout: int = 10, retries: int = 3):
        if base_url:
            self.validate_base_url(base_url)
            self.base_url = base_url
        self.timeout = timeout # For later implementation of timeout handling
        self.retries = retries # For later implementation of retry handling
        
    def validate_base_url(self, url):
        parsed_url = urlsplit(url)
                        
        if parsed_url.scheme != "https":
            raise ValueError("base URL must use HTTPS.")
        elif not parsed_url.netloc:
            # TODO: Add further validation for top level domains
            raise ValueError("base URL must have a valid location.")
        elif parsed_url.path or parsed_url.query or parsed_url.fragment:
            raise ValueError("base URL must not contain a path, query, or fragment.")
        pass
    
    def scrape_endpoint(self, endpoint: str = ""):
        if not self.base_url:
            raise ValueError("Base URL is not set. Please set the base URL before scraping.")
        
        full_url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.get(full_url, timeout=self.timeout)
            return response
        except Exception as e:
            raise Exception(f"An error occurred while making the request to {full_url}: {e}")
    
    def update_base_url(self, url):
        self.validate_base_url(url)
        self.base_url = url