from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from crawler.request import Request
from crawler.itemPipeline import itemPipeline
from crawler.item import Item


class Spider:
    def __init__(self, max_depth, scheduler):
        self.max_depth = max_depth
        self.scheduler = scheduler
        self.visited_urls = set()
        self.item_pipeline = itemPipeline()
        self.response_code = 0

    def parse(self, response, depth, base_domain, core_name):
        content_type = response.headers.get('Content-Type', '')
        if not self.is_html(content_type):
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        self.parse_links(soup, response.url, depth, base_domain)
        self.save_item(soup, response.url, core_name)
        return self.response_code

    def is_sameDomain(self, url, base_domainRoot):
        url_domain = urlparse(url).netloc
        return url_domain == base_domainRoot

    def create_item(self, soupHtml, pageURL):
        new_item = Item.create_item(soupHtml, pageURL)
        if new_item is not None:
            return new_item
        else:
            return None

    def is_html(self, content_type):
        return 'text/html' in content_type

    def parse_links(self, soup, response_url, depth, base_domain):
        links = soup.find_all('a', href=True)
        absolute_urls = [self.get_absolute_url(response_url, link['href']) for link in links]
        same_domain_urls = [url for url in absolute_urls if self.is_sameDomain(base_domainRoot=base_domain, url=url)]

        for url in same_domain_urls:
            if url not in self.visited_urls:
                self.visited_urls.add(url)
                if depth < self.max_depth:
                    new_request = Request(url, depth + 1)
                    self.scheduler.enqueue_request(new_request)

    def save_item(self, soup, url, core_name):
        new_item_created = self.create_item(soup, url)
        if new_item_created is not None:
            self.response_code = self.item_pipeline.save_item(new_item_created, core_name)

    def get_absolute_url(self, response_url, href):
        if href.startswith('http://') or href.startswith('https://'):
            return href
        else:
            return urljoin(response_url, href)
