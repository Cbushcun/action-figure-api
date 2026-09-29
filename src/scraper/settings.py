import os
from src.parser.json_manager import JSONManager

# Scraper settings
SCRAPER_SOURCES_JSON: str = os.getenv("SOURCES_JSON", "src/scraper/source_list.json")
SCRAPER_SOURCES = JSONManager().load_file(filepath=SCRAPER_SOURCES_JSON)
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")
SCRAPER_API_URL = os.getenv("SCRAPER_API_URL")