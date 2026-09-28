from bs4 import BeautifulSoup

class HTMLParser:
    def __init__(self: HTMLParser, html_content: str) -> None:
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def get_title(self):
        title_tag = self.soup.find('title')
        return title_tag.text if title_tag else None

    def get_meta_description(self):
        meta_tag = self.soup.find('meta', attrs={'name': 'description'})
        return meta_tag['content'] if meta_tag and 'content' in meta_tag.attrs else None

    def get_links(self):
        links = []
        for a_tag in self.soup.find_all('a', href=True):
            links.append(a_tag['href'])
        return links