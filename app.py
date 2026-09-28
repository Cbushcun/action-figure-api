import os

from dotenv import load_dotenv
from src.parsers.json_parser import JSONObject

if __name__ == "__main__":
    load_dotenv()
    sources: JSONObject = JSONObject(filepath=os.getenv("SOURCES_JSON"))
    print(type(sources.data[0]))