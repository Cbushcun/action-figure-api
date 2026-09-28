import requests

class Scraper:
    def __init__(self, base_url, timeout=10, retries=3):
        self.base_url = base_url
        self.timeout = timeout # For later implementation of timeout handling
        self.retries = retries # For later implementation of retry handling
    
    def scrape(self, endpoint):
        raise NotImplementedError("Subclasses must implement the scrape method.")