import os

from src.parsers.json_parser import JSONObject

if __name__ == "__main__":
    sources = JSONObject(filepath=os.getenv("SOURCES_JSON"))