from urllib.parse import urlparse


class Request:
    def __init__(self, url, depth=0):
        self.url = url
        self.depth = depth
        self.domain = self.extract_domain(url)

    def extract_domain(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc
