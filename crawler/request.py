from urllib.parse import urlparse


class Request:
    def __init__(self, url, depth=0):
        self.url = self.normalize_url(url)
        self.depth = depth
        self.domain = self.extract_domain(url)

    def extract_domain(self, url):
        parsed_url = urlparse(url)
        return parsed_url.netloc

    def normalize_url(self, url):
        if url.endswith('/'):
            return url
        else:
            return url + '/'
