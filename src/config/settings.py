import os

from src.parser.json_parser import JSONObject

from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

# Scraper settings
SCRAPER_SOURCES_JSON: Path = Path(os.getenv("SOURCES_JSON", "src/scraper/source_list.json"))
SCRAPER_SOURCES = JSONObject(filepath=SCRAPER_SOURCES_JSON).data