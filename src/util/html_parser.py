from bs4 import BeautifulSoup

class HTMLPage:
    def __init__(self: HTMLPage, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')
        
    def __str__(self: HTMLPage):
        return f"{self.soup}"

    def get_title(self):
        title_tag = self.soup.find('title')
        return title_tag.text if title_tag else None

    def get_meta_description(self):
        meta_tag = self.soup.find('meta', attrs={"name": "description"})
        return meta_tag['content'] if meta_tag and 'content' in meta_tag.attrs else None