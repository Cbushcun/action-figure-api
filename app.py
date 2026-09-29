from src.util import HTMLPage
from src.scraper import Scraper

from src.database import DatabaseClient

if __name__ == "__main__":
#    scraper = Scraper()
#    search_text = input("Enter text to search: ")
#    adjusted_text = search_text.replace(" ", "+")
#    res = scraper.scrape(f"https://www.bigbadtoystore.com/Search?SearchText={adjusted_text}")
#    html = HTMLPage(res.content)
#    
#    print(html.soup.find_all("h3",{"class":"product-card-title"}))
    db = DatabaseClient()    