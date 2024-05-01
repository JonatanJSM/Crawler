from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from crawler.request import Request


class Spider:
    def __init__(self, max_depth, scheduler):
        self.max_depth = max_depth
        self.scheduler = scheduler
        self.visited_urls = set()

    def parse(self, response, depth, base_domain):
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' not in content_type:
            print(f"Ignorando URL {response.url} porque no contiene contenido HTML")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            absolute_url = urljoin(response.url, href)

            if not self.is_sameDomain(base_domainRoot=base_domain, url=absolute_url):
                continue

            if absolute_url in self.visited_urls:
                continue
            else:
                self.visited_urls.add(absolute_url)
            if depth < self.max_depth:
                new_request = Request(absolute_url, depth + 1)
                self.scheduler.enqueue_request(new_request)

        title = soup.title.text.strip()
        body = soup.get_text().strip()
        data = {'title': title, 'body': body}
        print(f"Guardando datos en Solr: {data}")

    def is_sameDomain(self, url, base_domainRoot):
        url_domain = urlparse(url).netloc
        return url_domain == base_domainRoot
